import pandas
import requests
import json
import boto3
from datetime import datetime
import numpy
import threading
import os


Authorization = os.getenv('Authorization')
headers = {
    "Authorization": Authorization,
    "accept": "application/json"
}

bucketName = 'data-lake-do-berg'
s3_client = boto3.client('s3')

# Função para gravar os atores no bucket s3

def gravarAtores(objetoJson, nomeArquivo):

    data_atual = datetime.now()
    data_formatada = data_atual.strftime('%Y/%m/%d')
    key = f'Raw/TMDB/JSON/Atores/{data_formatada}/{nomeArquivo}'

    s3_client.put_object(Bucket=bucketName, Key=key, Body=objetoJson)

# Função que retorna atores da API

def retornarAtores(imdbID):
    url = f'https://api.themoviedb.org/3/find/{imdbID}?external_source=imdb_id'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        if data.get("movie_results"):
            obraID = data["movie_results"][0]["id"]

            url = f'https://api.themoviedb.org/3/movie/{obraID}/credits'
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                data = response.json()
                return data
            else:
                return None            
        else: 
            return None
        
    return None

# Função para buscar atores e salvá-los no bucket s3

def buscarAtores(moviesIDs, threadName):    
    atores = {}
    contador = 0
    numeroArquivo = 0

    ultimoIndice = len(moviesIDs) - 1
    for indice, id in enumerate(moviesIDs):
        contador += 1

        atorJson = retornarAtores(id)
        if atorJson is not None:
            atores[id] = atorJson

        if contador % 100 == 0:
            numeroArquivo += 1            
            jsonData = json.dumps(atores)
            arquivo = f'Atores-{threadName}-{numeroArquivo}.json'
            gravarAtores(jsonData, arquivo)
            atores = {}

        elif indice == ultimoIndice:
            numeroArquivo += 1            
            jsonData = json.dumps(atores)
            arquivo = f'Atores-{threadName}-{numeroArquivo}.json'
            gravarAtores(jsonData, arquivo)

# Função para criação de threads de execução concorrente

def executarThreads(dfAtores):
    valores = ['Drama,Romance', 'Drama', 'Romance']
    condicao = dfAtores['genero'].isin(valores)
    
    dfAtoresNormalizado = dfAtores[condicao].drop_duplicates()

    colunaMovieID = dfAtoresNormalizado["id"].to_numpy()
    arraysMoviesID = numpy.array_split(colunaMovieID, 60)
    arraysMoviesID = numpy.array(arraysMoviesID, dtype=object)

    threads = []
    
    for i in range(60):
        threadName = f'T{i}'
        thread = threading.Thread(target=buscarAtores, args=(arraysMoviesID[i], threadName))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

#  Função lambda de inicialização do código
 
def lambda_handler(event, context):
    s3_file_name = 'Raw/Local/CSV/Movies/2024/05/09/movies.csv'
    objeto = s3_client.get_object(Bucket=bucketName, Key=s3_file_name)
    dfAtores = pandas.read_csv(objeto['Body'], sep='|', usecols=['id', 'genero'])
    executarThreads(dfAtores)
 
    return {
        'statusCode': 200,
        'body': "Dados salvos com sucesso!"
    }
