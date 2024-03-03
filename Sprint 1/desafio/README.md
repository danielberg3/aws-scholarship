# Realização do Desafio

## Comandos para configuração do ambiente e criação de arquivos e diretórios


1. Criar diretório ecommerce:
    
    ```bash
    mkdir ecommerce
    ```
1. Entrar no diretório ecommerce:
    
    ```bash
    cd ecommerce
    ```
1. Criar arquivo executável a ser programada a execução:
    
    ```bash
    touch processamento_de_vendas.sh
    ```
1. Tornar arquivo executável:
    
    ```bash
    chmod a+x processamento_de_vendas.sh
    ```
1. Criar arquivo executável a ser executado manualmente:
    
    ```bash
    touch consolidados_de_processamento_de_vendas.sh
    ```
1. Tornar arquivo executável:
    
    ```bash
    chmod a+x consolidados_de_processamento_de_vendas.sh
    ```
1. Comando para adicionar execução programada do arquivo processamento_de_vendas.sh:
    
    ```bash
    crontab -e
    ```
1. Linha a ser adicionada para que o script execute automaticamente:
    
    ```bash
    27 15 * * 1-4 /bin/bash /home/daniel/Documentos/aws-scholarship/Sprint\ 1/desafio/ecommerce/processamento_de_vendas.sh
    ```


## Criação do projeto

Antes de iniciar é necessário adicionar o arquivo [dados_de_vendas.csv](ecommerce/dados_de_vendas.csv) dentro da pasta ecommerce.

Após realizar a configuração do ambiente está na hora de construção da lógica de funcionamento dos scripts, a mesma pode ser observada dentro do arquivo [processamento_de_venda.sh](ecommerce/processamento_de_vendas.sh), o qual cria os arquivos de relatório e os zip de backup automaticamente de segunda à quinta às 15:27. Também foi criado o arquivo [consolidador_de_processamento_de_venda.sh](ecommerce/consolidador_de_processamento_de_vendas.sh), o qual ao ser executado manualmente gera um relatório final com todos os relatórios dentro da pasta de backup.

## Evidências de execução

[Ver processo de execução](evidencias/README.md)