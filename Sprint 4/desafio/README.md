---
jupyter:
  jupytext:
    cell_metadata_filter: -all
    custom_cell_magics: kql
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.11.2
---

# Desafio


## Etapa 1

### Nesta etapa foi criado um arquivo [Dockerfile](Etapa%20I%20&%20II/Dockerfile) com os seguintes passos:

1. Foi definido que a imagem do python seria utilizada na imagem criada.
2. Foi criado o diretório de trabalho /app.
3. Foi feita uma cópia do arquivo [caguru.py](Etapa%20I%20&%20II/carguru.py) para dentro do diretório de trabalho.
4. Foi definido o comando para ser executado dentro do container: *python carguru.py*.

* Em seguida, para criar a imagem, dentro do diretório onde se encontra o arquivo Dockerfile (Etapa I & II) foi executado o comando:

```PowerShell
docker build -t carguru .
```

* Criação da imagem:

!['Criação imagem docker'](Etapa%20I%20&%20II/images/criacao-image.png)


* Por fim foi criado o container a partir da imagem carguru com o seguinte comando:

```PowerShell
  docker run --name container-carguru carguru
```

* Criação do container: 

!['Criação container docker'](Etapa%20I%20&%20II/images/criacao-container.png)

## Etapa 2

É possível reutilizar um container, para isso basta executar o seguinte comando:

```PowerShell
  docker start container-carguru
```

## Etapa 3

### Nesta etapa foi criado o arquivo [gerar-hash.py](Etapa%20III/gerar-hash.py) com os seguintes passos:

1. Foi feita a importação da biblioteca hashlib.
2. Foi criado um while infinito.
3. Foi feita a leitura de uma string a patir de um input.
4. Foi criada uma condição para quebrar o laço caso a string esteja vazia.
5. Foi criado um objeto hash do tipo sha-1.
6. O objeto foi atualizado com o valor da string utilizando o pradrão de encode utf-8.
7. Por fim foi exibido o valor da variável hash através do método hexdigest, o qual retorna o hexadecimal de hash.

### Logo após, foi criado um arquivo [Dockerfile](Etapa%20III/Dockerfile) com os seguintes passos:


1. Foi definido que a imagem do python seria utilizada na imagem criada.
2. Foi criado o diretório de trabalho /app.
3. Foi feita uma cópia do arquivo [gerar-hash.py](Etapa%20III/gerar-hash.py) para dentro do diretório de trabalho.
4. Foi definido o comando para ser executado dentro do container: *python gerar-hash.py*.

* Em seguida, para criar a imagem, dentro do diretório onde se encontra o arquivo Dockerfile (Etapa III) foi executado o comando:

```PowerShell
  docker build -t mascarar-dados .
```

* Geração da imagem:

!['Imagem mascarar-dados'](Etapa%20III/images/criacao-image.png)

* Comando para criar o container a partir da imagem e executar o mesmo de forma interativa:

```PowerShell
  docker run -it --name container-mascarar-dados mascarar-dados
```

* Geração do container:

!['Container container-mascarar-dados'](Etapa%20III/images/criacao-container.png)
