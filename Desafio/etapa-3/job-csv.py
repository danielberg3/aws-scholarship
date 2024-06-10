import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.types import StringType, IntegerType, DoubleType
from datetime import datetime
from pyspark.sql.functions import col, regexp_replace
from awsglue.dynamicframe import DynamicFrame


# Configuração do Glue para iniciar o JOB

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME','S3_INPUT_PATH_MOVIES', 'S3_INPUT_PATH_SERIES', 'S3_OUTPUT_PATH'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

target_path = args['S3_OUTPUT_PATH']


# Função para criar arquivo parquet

def criarArquivos(arquivo, dataFrame):

    # Captura da  data atual para montar o caminho
    data_atual = datetime.now()
    data_formatada = data_atual.strftime('%Y/%m/%d')


    # Definição do caminho para salvar a partir do tipo de arquivo
    if arquivo == 'movies':
        caminhoDados = f'{target_path}/Movies/{data_formatada}'    
    else:
        caminhoDados = f'{target_path}/Series/{data_formatada}'  


    # Salvamento dos dados no formato parquet
    glueContext.write_dynamic_frame.from_options(
    frame = dataFrame,
    connection_type = "s3",
    connection_options = {"path": caminhoDados},
    format = "parquet")


# Função para limpar dados dos arquivos CSV

def limparDados(arquivo):
    
    # Definição do caminho de busca a partir do tipo de arquivo
    if arquivo == 'movies':
        source_file = args['S3_INPUT_PATH_MOVIES']
    else:
        source_file = args['S3_INPUT_PATH_SERIES']


    # Leitura dos arquivos CSV no caminho de busca
    df = glueContext.create_dynamic_frame.from_options(
    "s3",
    {
    "paths": [
    source_file
    ]
    },
    "csv",
    {"withHeader": True, "separator":"|"},
    )

    # Conversão do dataFrame dinâmico em um dataframe spark
    df = df.toDF()

    # Captura dos dados dos arquivos CSV que sejam exclusivos de drama e romance
    valores = ['Drama,Romance', 'Drama', 'Romance']
    condicao = col('genero').isin(valores)
    df = df.filter(condicao)

    # Substituir '\N' por strings vazias e zeros em colunas específicas
    df = df.withColumn('id', regexp_replace(col('id'), r'\\N', '').cast(StringType()))\
    .withColumn('tituloPincipal', regexp_replace(col('tituloPincipal'), r'\\N', '').cast(StringType()))\
        .withColumn('tituloOriginal', regexp_replace(col('tituloOriginal'), r'\\N', '').cast(StringType()))\
            .withColumn('anoLancamento', regexp_replace(col('anoLancamento'), r'\\N', '0').cast(IntegerType()))\
                .withColumn('tempoMinutos', regexp_replace(col('tempoMinutos'), r'\\N', '0').cast(IntegerType()))\
                    .withColumn('notaMedia', regexp_replace(col('notaMedia'), r'\\N', '0').cast(DoubleType()))\
                        .withColumn('numeroVotos', regexp_replace(col('numeroVotos'), r'\\N', '0').cast(IntegerType()))\
                            .withColumn('generoArtista', regexp_replace(col('generoArtista'), r'\\N', '').cast(StringType()))\
                                .withColumn('personagem', regexp_replace(col('personagem'), r'\\N', '').cast(StringType()))\
                                    .withColumn('nomeArtista', regexp_replace(col('nomeArtista'), r'\\N', '').cast(StringType()))\
                                        .withColumn('anoNascimento', regexp_replace(col('anoNascimento'), r'\\N', '0').cast(IntegerType()))\
                                            .withColumn('anoFalecimento', regexp_replace(col('anoFalecimento'), r'\\N', '0').cast(IntegerType()))\
                                                .withColumn('profissao', regexp_replace(col('profissao'), r'\\N', ''))\
                                                    .withColumn('titulosMaisConhecidos', regexp_replace(col('titulosMaisConhecidos'), r'\\N', '').cast(StringType()))


    # Coluna adicional a ser tratada caso o CSV seja de series
    if arquivo ==  'series':
        df = df.withColumn('anoTermino', regexp_replace(col('anoTermino'), r'\\N', '0').cast(IntegerType()))

    # Remoção de linhas duplicadas
    df = df.dropDuplicates()

    # Informando que o dataframe deve originar apenas um arquivo
    df = df.coalesce(1)

    # Conversão do data frame em um único dynamic_frame
    dynamic_frame = DynamicFrame.fromDF(df, glueContext, "dynamic_frame")

    criarArquivos(arquivo, dynamic_frame)


limparDados('movies')
limparDados('series')

job.commit()