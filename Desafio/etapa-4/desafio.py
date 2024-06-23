import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, collect_set, col, concat_ws, monotonically_increasing_id, explode, split
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_iNPUT_LOCAL_MOVIES', 'S3_iNPUT_LOCAL_SERIES', 'S3_iNPUT_TMDB_MOVIES', 'S3_OUTPUT_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

s3_input_local_movies = args['S3_iNPUT_LOCAL_MOVIES']
s3_input_local_series = args['S3_iNPUT_LOCAL_SERIES']
s3_input_tmdb_movies = args['S3_iNPUT_TMDB_MOVIES']
s3_output_path = args['S3_OUTPUT_PATH']


df_moviesLocal = spark.read.parquet(s3_input_local_movies)
df_seriesLocal = spark.read.parquet(s3_input_local_series)
df_moviesTMDB = spark.read.parquet(s3_input_tmdb_movies)

# Unir dados de filmes do arquivo csv com os dados de filme pesquisados na api
df_movies = df_moviesLocal.join(df_moviesTMDB,  df_moviesLocal.id == df_moviesTMDB.imdb_id, "left") \
    .select(
        df_moviesTMDB.adult,
        df_moviesTMDB.imdb_id,
        df_moviesTMDB.origin_country,
        df_moviesTMDB.overview,
        df_moviesTMDB.popularity,
        df_moviesLocal.id,
        df_moviesLocal.tituloPincipal,
        df_moviesLocal.tituloOriginal,
        df_moviesLocal.anoLancamento,
        df_moviesLocal.tempoMinutos,
        df_moviesLocal.genero,
        df_moviesLocal.notaMedia,
        df_moviesLocal.numeroVotos,
        df_moviesLocal.generoArtista,
        df_moviesLocal.nomeArtista,
        df_moviesLocal.anoNascimento,
        df_moviesLocal.anoFalecimento,
        df_moviesLocal.profissao,
        df_moviesLocal.titulosMaisConhecidos,
        df_moviesLocal.midia
    )

# Selecionar informações dos atores dentro dos arquivos csv
df_atores_series = df_seriesLocal.select(col("id"), col("generoArtista"), col("nomeArtista"), col("anoNascimento"), col("anoFalecimento"), col("profissao"), col("titulosMaisConhecidos"))
df_atores_movies = df_moviesLocal.select(col("id"), col("generoArtista"), col("nomeArtista"), col("anoNascimento"), col("anoFalecimento"), col("profissao"), col("titulosMaisConhecidos"))

# Juntar as informações de atores do csv de filmes e do csv de séries
df_atores = df_atores_series.unionByName(df_atores_movies)


# Agrupar pelas informações de atores concatenando os ids das obras
df_atores = df_atores.groupBy(
    col("generoArtista"),
    col("nomeArtista"),
    col("anoNascimento"),
    col("anoFalecimento"),
    col("profissao"),
    col("titulosMaisConhecidos")
).agg(
    concat_ws(",", collect_set(col("id").cast("string"))).alias("idsFilmesSeries")
)

# Gerar um id único para cada ator
df_atores = df_atores.withColumn("idAtor", monotonically_increasing_id() + 1)

# Criar dimensão de filmes selecionando colunas específicas
dim_movies = df_movies.select(
    "adult",
    "origin_country",
    "overview",
    "popularity",
    "id",
    "tituloPincipal",
    "tituloOriginal",
    "anoLancamento",
    "tempoMinutos",
    "genero",
    "notaMedia",
    "numeroVotos"
)

# Criar dimensão de séries selecionando colunas específicas
dim_series = df_seriesLocal.select(
    "id",
    "tituloPincipal",
    "tituloOriginal",
    "anoLancamento",
    "anoTermino",
    "tempoMinutos",
    "genero",
    "notaMedia",
    "numeroVotos"
)

# Criar dimensão de atores selecionando colunas específicas
dim_actors = df_atores.select(
    "generoArtista",
    "nomeArtista",
    "anoNascimento",
    "anoFalecimento",
    "profissao",
    "titulosMaisConhecidos",
    "idAtor"
)

# Schema para dimensão de categoria
schema = StructType([
    StructField("idCategoria", IntegerType(), True),
    StructField("TipoMidia", StringType(), True)
])

#  Valores da dimensão de categoria
valores = [(1, "movie"), (2, "serie")]

# Criação da dimensão de categoria
dim_category = spark.createDataFrame(valores, schema)

# explosão da coluna idsFilmesSeries para gerar uma linha para cada id contido dentro do campo
tabela_fato = df_atores.withColumn("idObra", explode(split(col("idsFilmesSeries"), ",")))

#  Criação da tabela fato selecionando as colunas idObra e idAtor.
tabela_fato = tabela_fato.select(col("idObra"), col("idAtor"))

# Seleção das colunas id e midia dos dataframes de séries e filmes, em seguida a união dos dataframes resultantes
df_midia_series = df_seriesLocal.select(col("id"), col("midia")).dropDuplicates()
df_midia_movies = df_moviesLocal.select(col("id"), col("midia")).dropDuplicates()
df_midia_series_movies = df_midia_series.unionByName(df_midia_movies)




# Criação de um novo dataframe contendo o id de filmes e série e o id da categoria através do uso do join
df_categoria_midia = df_midia_series_movies.join(dim_category,  df_midia_series_movies.midia == dim_category.TipoMidia, "inner")\
    .select(        
        df_midia_series_movies.id,
        dim_category.idCategoria
    )

#  originando nova tabela fato com as colunas idObra, idAtor e idCategoria a partir do join
tabela_fato = tabela_fato.join(df_categoria_midia,  tabela_fato.idObra == df_categoria_midia.id, "inner")\
    .select(
        tabela_fato.idObra,
        tabela_fato.idAtor,
        df_categoria_midia.idCategoria
    )
    

# Salvando os arquivos parquet dentro da camada refined do s3
tabela_fato.coalesce(1).write.parquet(s3_output_path + 'tabela_fato')
dim_category.coalesce(1).write.parquet(s3_output_path + 'dim_category')
dim_actors.coalesce(1).write.parquet(s3_output_path + 'dim_actors')
dim_series.coalesce(1).write.parquet(s3_output_path + 'dim_series')
dim_movies.coalesce(1).write.parquet(s3_output_path + 'dim_movies')

job.commit()