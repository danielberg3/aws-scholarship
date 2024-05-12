from dotenv import load_dotenv
import os
import logging
import boto3
from botocore.exceptions import ClientError
from datetime import datetime

# Carga das variáveis de ambiente na memória

load_dotenv()

# Atribuição das variáveis de ambiente as variáveis do python

access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
session_token= os.getenv("AWS_SESSION_TOKEN")
aws_region = os.getenv("AWS_REGION")
aws_bucket_name = "data-lake-do-berg"

#  Inicialização de um cliente para o serviço s3 utilizando boto3

s3_client = boto3.client(
    's3',
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key,
    aws_session_token=session_token,
    region_name=aws_region
)

# Função para criação do bucket 

def create_bucket(bucket_name):
    try:
        s3_client.create_bucket(Bucket=bucket_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


#  Função de upload do arquivo movies.csv

def upload_movies_csv(file, bucket_name):
    data_atual = datetime.now()
    data_formatada = data_atual.strftime('%Y/%m/%d')
    key = f'Raw/Local/CSV/Movies/{data_formatada}/movies.csv'

    with open(file, 'r') as data:
        s3_client.put_object(Bucket=bucket_name, Key=key, Body=data.read())


#  Função de upload do arquivo series.csv

def upload_series_csv(file, bucket_name):
    data_atual = datetime.now()
    data_formatada = data_atual.strftime('%Y/%m/%d')
    key = f'Raw/Local/CSV/Series/{data_formatada}/series.csv'

    with open(file, 'r') as data:
        s3_client.put_object(Bucket=bucket_name, Key=key, Body=data.read())


#  Chamada das funções

create_bucket(aws_bucket_name)
upload_movies_csv('dados/movies.csv', aws_bucket_name)
upload_series_csv('dados/series.csv', aws_bucket_name)
