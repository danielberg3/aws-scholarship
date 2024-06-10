import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import datetime
from pyspark.sql.types import StringType, DoubleType
from pyspark.sql.functions import lit, col, concat_ws

# Configuração do Glue para iniciar o JOB

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_OUTPUT_PATH'])

input_path = args['S3_INPUT_PATH']
output_path = args['S3_OUTPUT_PATH']

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)


# Criação do dynamicFrame a partir dos arquivos json
dynamicFrame = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={
        "paths": [input_path]
    },
    format="json",
    format_options={
        "multiline": True
    }
)

# Conversão do dynamicFrame em dataFrame spark e especificação de que os dados devem formar um único arquivo
df = dynamicFrame.toDF().coalesce(1)

# Captura da data atual para utilizar no particionamento do parquet
data = datetime.date.today() 
data_formatada = f"{data.year}-{data.month}-{data.day}"

# Seleção das colunas a serem utilizadas
df = df.select(col('adult'), col('budget'), col('imdb_id'), col('origin_country'), col('overview'), col('popularity'), col('revenue'))


# Conversão das colunas e adição da coluna etl_date para particionamento do parquet
df = df.withColumn('adult', col('adult').cast(StringType()))\
    .withColumn('budget', col('budget').cast(DoubleType()))\
        .withColumn('imdb_id', col('imdb_id').cast(StringType()))\
            .withColumn("origin_country", concat_ws(",", col("origin_country")).cast(StringType()))\
                .withColumn('overview', col('overview').cast(StringType()))\
                    .withColumn('popularity', col('popularity').cast(DoubleType()))\
                        .withColumn('revenue', col('revenue').cast(DoubleType()))\
                            .withColumn('etl_date', lit(data_formatada).cast(StringType()))


# Escrita do arquivo no caminho de saída particionado pelo elt_date
df.write.partitionBy('etl_date').parquet(output_path)

job.commit()