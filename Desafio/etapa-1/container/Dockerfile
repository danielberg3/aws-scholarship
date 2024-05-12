FROM python

# Criação de diretório de trabalho

WORKDIR /app

# Instalação das dependências 

RUN pip install python-dotenv
RUN pip install boto3

# Definição do fuso horário a ser utilizado dentro do container

ENV TZ=America/Maceio
RUN apt-get update && apt-get install -y tzdata
RUN ln -fs /usr/share/zoneinfo/$TZ /etc/localtime && dpkg-reconfigure -f noninteractive tzdata

# Copia dos arquivos desafio.py e .env para dentro da imagem

COPY desafio.py .
COPY .env .

# Criação do diretório de dados para ser linkado como volume a um diretório do host

RUN mkdir dados

#  Comando a ser executado na criação do container

CMD ["python", "desafio.py"]

