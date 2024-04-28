from dotenv import load_dotenv
import os
import logging
import boto3
from botocore.exceptions import ClientError
import pandas as pd
from io import StringIO


load_dotenv()

with open('primeiro-comando.sql', 'r') as arquivo:
    primeira_query = arquivo.read()



with open('segundo-comando.sql', 'r') as arquivo:
    segunda_query = arquivo.read()


access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
session_token= os.getenv("AWS_SESSION_TOKEN")
aws_region = os.getenv("AWS_REGION")
aws_bucket_name = "data-csv-for-consultas"
aws_account_id = os.getenv("ACCOUNT_ID")


s3_client = boto3.client(
    's3',
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key,
    aws_session_token=session_token,
    region_name=aws_region
)


def create_bucket(bucket_name):
    try:
        s3_client.create_bucket(Bucket=bucket_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def upload_csv(file, bucket_name):
    with open(file, 'r') as data:
        s3_client.put_object(Bucket=bucket_name, Key=file, Body=data.read())
        
def query_csv(bucket_name, account_id, query_consulta):
    response = s3_client.select_object_content(
        Bucket=bucket_name,
        Key='disciplinas-ifal-2022.csv',
        Expression=query_consulta,
        ExpressionType='SQL',
        RequestProgress={
            'Enabled': False
        },
        InputSerialization={
            'CSV': {
                'FileHeaderInfo': 'USE',
                'RecordDelimiter': '\n',
                'FieldDelimiter': ';',
                'QuoteCharacter': '"',
            }
        },
        OutputSerialization={
            'CSV': {
                'QuoteFields': 'ASNEEDED',
                'RecordDelimiter': '\n',
                'FieldDelimiter': ',',
                'QuoteCharacter': '"',
            },
        },
        ExpectedBucketOwner=account_id
    )

    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        for event in response['Payload']:
            if 'Records' in event:
                records = event['Records']['Payload'].decode('utf-8')
                return records
    else:
        print('Falha na requisição')
        return 0

# CRIAR BUCKET S3

# create_bucket(aws_bucket_name)

# SUBIR ARQUIVO .CSV PARA DENTRO DO BUCKET

# upload_csv("disciplinas-ifal-2022.csv", aws_bucket_name)


dados_primeira_consulta = query_csv(aws_bucket_name, aws_account_id, primeira_query)
colunas = ['disciplina', 'curso', 'campus', 'modalidade', 'carga_horaria', 'vagas_2020-ano_atual']
dados = pd.read_csv(StringIO(dados_primeira_consulta), header=None, names=colunas)

print(dados)

dados_segunda_consulta = query_csv(aws_bucket_name, aws_account_id, segunda_query)
informacao = dados_segunda_consulta.split(",")


print(f'Turmas de matemática: {informacao[0]}')    
print(f'Total de vagas: {informacao[1]}')
