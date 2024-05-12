# Exercícios


## Bucket S3

* Criação do bucket dentro do Amazon S3 contendo os arquivos para realização das próximas etapas:

![sao-bucket](../evidencias/s3-bucket.png)

* Site estático renderizado a partir do arquivo index.html dentro do bucket:

![site-estatico](../evidencias/site-estatico-s3.png)

## Amazon Athena

* Query dentro do Amazon Athena para consulta dos 3 nomes mais utilzados em cada decáda conforme dados do csv que está armazenado no bucket:

![query-athena](../evidencias/query-athena.png)

* Resultado da query:

![resultado-query-athena](../evidencias/resultado-query-athena.png)

## Função Lambda

* Dockerfile com instruções para gerar arquivo com layer personalida para função Lambda:

![dockerfile-layer-lambda](../evidencias/dockerfile-container-imagem.png)

* Resultado da execução da função lambda de comunicação com o bucket:

![execucao-funcao-lambda](../evidencias/execucao-funcao-lambda.png)