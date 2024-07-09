import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, collect_set, concat_ws, monotonically_increasing_id, explode, split

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_iNPUT_LOCAL_MOVIES', 'S3_iNPUT_TMDB_MOVIES', 'S3_OUTPUT_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

s3_input_local_movies = args['S3_iNPUT_LOCAL_MOVIES']
s3_input_tmdb_movies = args['S3_iNPUT_TMDB_MOVIES']
s3_output_path = args['S3_OUTPUT_PATH']

df_moviesLocal = spark.read.parquet(s3_input_local_movies).alias("local")
df_moviesTMDB = spark.read.parquet(s3_input_tmdb_movies).alias("tmdb")

# Unir dados de filmes do arquivo csv com os dados de filme pesquisados na api
df_movies = df_moviesLocal.join(df_moviesTMDB, col("local.id") == col("tmdb.imdb_id"), "inner") \
    .select(
        col("tmdb.adult"),
        col("tmdb.imdb_id"),
        col("tmdb.origin_country"),
        col("tmdb.overview"),
        col("tmdb.popularity"),
        col("local.id"),
        col("local.tituloPincipal"),
        col("local.tituloOriginal"),
        col("local.anoLancamento"),
        col("local.genero"),
        col("local.tempoMinutos"),
        col("local.notaMedia"),
        col("local.numeroVotos"),
        col("local.generoArtista"),
        col("local.nomeArtista"),
        col("local.anoNascimento"),
        col("local.anoFalecimento"),
        col("local.profissao"),
        col("local.titulosMaisConhecidos"),
        col("local.midia")
    )

# Selecionar informações dos atores dentro do arquivo movies.csv
df_atores = df_movies.select(col("id"), col("generoArtista"), col("nomeArtista"), col("anoNascimento"), col("anoFalecimento"), col("profissao"), col("titulosMaisConhecidos"))

# Agrupar pelas informações de atores concatenando os ids das obras
df_atores = df_atores.groupBy(
    col("generoArtista"),
    col("nomeArtista"),
    col("anoNascimento"),
    col("anoFalecimento"),
    col("profissao"),
    col("titulosMaisConhecidos")
).agg(
    concat_ws(",", collect_set(col("id").cast("string"))).alias("idsFilmes")
)

# Gerar um id único para cada ator
df_atores = df_atores.withColumn("idAtor", monotonically_increasing_id() + 1)

# Criar dimensão de filmes selecionando colunas específicas
dim_movies = df_movies.select(
    "adult",
    "origin_country",
    "overview",
    "id",
    "tituloPincipal",
    "tituloOriginal",
    "anoLancamento",
    "genero",
    "tempoMinutos"
).dropDuplicates(["id"])

dim_movies = dim_movies \
    .withColumnRenamed("adult", "adulto") \
    .withColumnRenamed("origin_country", "paisDeOrigem") \
    .withColumnRenamed("overview", "resumo") \
    .withColumnRenamed("tituloPincipal", "tituloPrincipal")


# Explosão da coluna idsFilmesSeries para gerar uma linha para cada id contido dentro do campo
df_atores = df_atores.withColumn("idObra", explode(split(col("idsFilmes"), ",")))

# Criar dimensão de atores selecionando colunas específicas
dim_actors = df_atores.select(
    "generoArtista",
    "nomeArtista",
    "anoNascimento",
    "anoFalecimento",
    "profissao",
    "titulosMaisConhecidos",
    "idAtor"
).dropDuplicates(["idAtor"]).withColumnRenamed("idAtor", "id")


# Criação da tabela fato selecionando as colunas idObra e idAtor.
fato_filmes = df_atores.select(col("idObra"), col("idAtor"))

# Adicionando informações de filmes à tabela a partir de dados de filmes
fato_filmes = fato_filmes.join(df_movies.alias("dfm"), col("idObra") == col("dfm.id"), "inner") \
    .select(
        col("idObra"),
        col("idAtor"),
        col("dfm.popularity"),
        col("dfm.notaMedia"),
        col("dfm.numeroVotos")
    ).withColumnRenamed("popularity", "popularidade").dropDuplicates()

# Salvando os arquivos parquet dentro da camada refined do s3
fato_filmes.coalesce(1).write.parquet(s3_output_path + 'movies/' + 'fato_filmes')
dim_movies.coalesce(1).write.parquet(s3_output_path + 'movies/' + 'dim_movies')
dim_actors.coalesce(1).write.parquet(s3_output_path + 'movies/' + 'dim_actors')

job.commit()
