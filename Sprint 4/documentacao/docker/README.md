---
jupyter:
  jupytext:
    cell_metadata_filter: -all
    custom_cell_magics: kql
    main_language: shell script
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.11.2
  kernelspec:
    display_name: base
    language: python
    name: python3
---

# Docker


Docker é uma ferramenta que simula uma máquina virtual, porém com menos exigências. A partir dela podemos criar os famosos containers, que se isolam do ambiente externo, permitindo que as tarefas possam ser executadas com as configurações necessárias ao projeto, além de ser mais performático, pois utilizam apenas aquilo que é necessário


## Containers vs Imagens

Imagens são blocos de códigos que definem as instruções de execução de um projeto, enquanto containers são os ambientes gerados pela ferramenta docker e que executam as imagens.

## Sumário

1. [Trabalhando com containers](#trabalhando-com-containers)
2. [Criando imagens e avançando em containers](#criando-imagens-e-avançando-em-containers)
3. [Volumes](#volumes)
4. [Conectando containers com network](#conectando-containers-com-network)
5. [Docker Compose](#docker-compose)
6. [Docker Swarm](#docker-swarm)
7. [Kubernets](#kubernets)





## Trabalhando com containers


Rodar imagem docker

```shell script
docker run ubuntu
```

Verificar containers rodando

```shell script
docker ps
```

Verficar todos os containers (os que estão rodando e os que não estão)

```shell script
docker ps -a
```

Rodar container de forma interativa

```shell script
docker run -it node
```


Rodar container em background

```shell script
docker run -d nginx
```

Expor portas

```shell script
docker run -d -p 80:80 nginx
```

Parar container

```shell script
docker stop 744f7bc04a05
docker stop studyDB
```

Reiniciar container

```shell script
docke start 744f7bc04a05
docker start studyDB
```

Nomear container

```shell script
docker run -d nginx --name app_nginx
```

Ver logs do container

```shell script
dokcer logs -f app_nginx
```

Remover container docker

```shell script
docker rm 744f7bc04a05
docker rm app_nginx
```

## Criando imagens e avançando em containers


Imagens são arquivos que programamos para que o container execute um conjunto de ações. Dentro delas temos imagens bases, diretório base, comando a serem executados porta da aplicação e etc. Assim as instruções serão executadas em camadas.


Criando Dockerfile

```shell script
# arquivo: Dockerfile

FROM node

WORKDIR /app

COPY package*.json .

RUN npm install

COPY . .

EXPOSE 3000

CMD ["node", "app.js"]

# construir a imagem 

docker build .

# executar a imagem

docker run -d -p 3000:3000 --name meu_node 744f7bc04a05
```

Baixar imagem localmente

```shell script
docker pull python
```

Ver informações sobre o comando

```shell script
docker run --help
```

Nomear imagem

```shell script
docker tag 744f7bc04a05 minha_imagem
```

Criar diferentes versões da imagem

```shell script
docker tag 744f7bc04a05 minha_imagem:minha_tag
```

Criar imagem já com o nome e a tag

```shell script
docker build -t meu_node:minha_tag .
```

Reiniciar container em modo interativo

```shell script
docker start -i meu_node
```

Remover imagem

```shell script
docker rmi meu_node:minha_tag
```

Remover imagens e containers não utilizados

```shell script
docker system prune --help
```

Remover container de forma automática após execução

```shell script
docker start -i  --rm meu_node
```

Copiar arquivo de dentro container para a máquina

```shell script
docker cp meu_node:/app/app.js ./copia/
```

Ver informações sobre o container que está em execução

```shell script
docker top meu_node
```

Inspecionar o container

```shell script
docker inspect meu_node
```

Ver informações sobre todos os containers que estão executando

```shell script
docker stats
```



```shell script

```


## Volumes

A maneira para persistir dados fora de um container


Volume anônimo

```shell script
docker run -v /data meu_node
```

Ver volume anônimo

```shell script
docker volume ls
```

Volume nomeado

```shell script
docker run -v meu_volume:/caminho_pasta_volumes meu_node
```

Bind mount (tornar o volume disponível no host)

```shell script
docker run -v /home/daniel/Documentos/aws-scholarship/Sprint 4/documentacao/docker:/caminho_pasta_volumes meu_node
```

É possível linkar o projeto do host com o docker através do bind mount de forma que atualizações ho host refletirão no projeto dentro do docker

```shell script
docker run -v /home/daniel/Documentos/aws-scholarship/Sprint 4/documentacao/docker:/caminho_para_workdir meu_node
```


Criar volume manualmente

```shell script
docker volume create meu_volume
```

Listar todos os volumes

```shell script
docker volume ls
```

Inspecionar volume

```shell script
docker volume inspect meu_volume
```

Remover volume (apaga também os dados)
É necessário remover os container que estejam usando o volume

```shell script
docker volume rm meu_volume
```

Remover todos os volumes que não estão sendo utilizados.

```shell script
docker volume prune
```

Criar volume apenas de leitura

```shell script
docker run -v /home/daniel/Documentos/aws-scholarship/Sprint 4/documentacao/docker:/caminho_pasta_volumes:ro meu_node
```

## Conectando containers com network


É a forma de conectar 2 ou mais containers para que possam se comunicar, ou conectar o container com ferramentas externas como uma API, ou até mesmo realizar a comunicação com o host.


Os dois principais tipos de rede são: bridge e host. Sendo a bridge utilizada para fazer a comunicação entre containers e host para comunicar o container ao host.


Verificar redes existentes

```shell script
docker network ls
```

Criar rede (a rede padrão é do tipo bridge)

```shell script
docker network create minha_rede
```

Criar rede com drive específico

```shell script
docker network create -d host minha_rede
```

Remover redes

```shell script
docker network rm minha_rede
```

Remover redes em massa

```shell script
docker network prune
```

Conectar container a uma rede manualmente

```shell script
docker network connect minha_rede meu_container
```

Desconectar container de uma rede

```shell script
docker network disconnect minha_rede meu_container
```

Ver informações sobre uma rede

```shell script
docker network inspect minha_rede
```


## Docker Compose

É uma ferramenta que permite a criação de uma arquivo que roda vários containers de uma só vez.


Exemplo de arquivo docker compose

```shell script
version: '3.4'

services:
  db:
    build: ./mysql/
    restart: always
    env_file:
      - ./config/db.env
    ports:
      - "3306:3306"
    networks:
      - dockercompose
    volumes:
      - ./mysql/schema.sql:/docker-entrypoint-initdb.d/init.sql
  
  flask:
    depends_on: 
      - db
    build: ./flask/
    ports:
      - "5000:5000"
    restart: always
    volumes:
      - "H:\\20_DOCKER\\arquivos\\5_compose\\6_bind_mount_compose\\flask:/app"
    networks: 
      - dockercompose

networks:
  dockercompose:
```

Executar arquivo docker-compose.yaml

```shell script
docker-compose up
```

Executar compose em background

```shell script
docker-compose up -d
```

Parar containers do docker compose

```shell script
docker compose down
```

Verificar serviços que o docker compose subiu

```shell script
docker compose ps
```

## Docker Swarm

É uma ferramenta utilizada para gerencia de containers. Muito utilizada em conjunto com servidores AWS para garantir que as máquinas que estejam usando o serviço não venha ter falhas.

Palavras chave:

- Nodes: Máquinas que participam do swarm.
- Manager Node: Node que que gerencia os demais nodes.
- Worker Node: Nodes funcionários, que recebem ordem do manager node.
- Service: Containers que manager node manda os worker node executar.
- Task: Comandos que os worker node recebem do manager node para ser executado.


Inciar node1 como principal

```shell script
docker swarm init --advertise-addr 192.168.0.18
```

Exibir nodes ativos

```shell script
docker node ls
```

Adicionar nodes ao swarm como workers

```shell script
docker swarm join --token SWMTKN-1-58kqvoh40fvrh346mi5koifcg7e8vho3p791sbudohaflprbmk-3qnv67uqqsdg9ctn352648efu 192.168.0.18:2377
```

Subir serviço no docker swarm

```shell script
docker service create --name nginxswarm -p 80:80 nginx
```

Ver serviços que estão executando dentro do swarm

```shell script
docker service ls
```

Remover serviço

```shell script
docker service rm yiv566gnm3ox
```

Criar réplicas de um serviço

```shell script
docker service create --name nginxreplicas --replicas 3 -p 80:80 nginx
```

Receber novamente comando de join-token

```shell script
docker swarm join-token manager
```

Desativar máquina do swarm

```shell script
docker swarm leave
```

Remover node do swarm

```shell script
docker node rm fhuayhqvmbv98c5gbgor5fy29
```

Inspecionar serviços

```shell script
docker service inspect q7h5ym46l3y8
```

Veficar containers que estão rodando um serviço (ID do serviço)

```shell script
docker service ps q7h5ym46l3y8
```


Rodar docker compose dentro do node 1

```shell script
sudo docker stack deploy -c docker-compose.yaml nginx_swarm
```

Replicar serviço nas máquinas

```shell script
sudo docker service scale nginx_swarm_web=3
```

Fazer com que o serviço não receba mais tasks

```shell script
sudo docker node update --availability drain c54isnjal12vgjw8si0op0of8
```

Atualizando imagem no swarm

```shell script
sudo docker service update --image nginx:1.18.0 pdq
```

Criar rede dentro do swarm

```shell script
docker network create --driver overlay swarm
```

Criando serviço dentro da rede criada

```shell script
docker service create --name nginxreplicas --replicas 3 -p 80:80 --network swarm nginx
```

Conectar serviço já criado a uma rede

```shell script
docker service update --network-add swarm 2ag5kmwetjxl
```

## Kubernets

É uma ferramenta de orquestração de máquinas, garantindo uma máquina centralize os processos e passe as tarefas para que as demais possam executar.

* Control Plane: Máquina que genencia as demais.
* Nodes: Máquinas que recebem ordens.
* Deployment: É a execução de uma imagem em um servidor (pod).
* Pod: Conjunto de containers executando em um node.
* Services: Utilizado para expor o servidor para utilização.
* Kubectl: CLI para o kubernets.


Iniciar minikube

```shell script
minikube start --driver=docker
```

Parar minikube

```shell script
minikube stop
```

Acessar dashboard do minikube

```shell script
minikube dashboard
minikube dashboard --url
```


Criar Deployment

```shell script
kubectl create deployment flask-deployment --image=matheusbattistti/flask-kub-projeto
```

Ver deployments

```shell script
kubectl get  deployments
```

Detalhar deployments

```shell script
kubectl describe deployments 
```

Checar pods

```shell script
kubectl get pods
```

Detalhar pods

```shell script
kubectl describe pods
```

Criar service

```shell script
kubectl expose deployment flask-deployment --type=LoadBalancer --port=5000
```

Gerar IP para o service

```shell script
minikube service flask-deployment
```

Ver serviços criados

```shell script
kubectl get services
```

Ver detalhes sobre um serviço

```shell script
kubectl describe services/flask-deployment
```

Criar réplicas do deployment

```shell script
kubectl scale deployment/flask-deployment --replicas=5
```

Verificar número de réplicas

```shell script
kubectl get rs
```


Reduzir número de réplicas

```shell script
kubectl scale deployment/flask-deployment --replicas=3
```

Atualizar imagem do projeto

```shell script
kubectl set image deployment/flask-deployment flask-kub-projeto=matheusbattisti/flask-kub-projeto:2
```

Desfazer alteração do projeto

```shell script
kubectl rollout undo deployment/flask-deployment
```

Deletar serviço

```shell script
kubectl delete service flask-deployment
```

Deletar deployment

```shell script
kubectl delete deployment flask-deployment
```

### Modo declarativo

* ApiVersion: Versão utilizada da ferramenta.
* Kind: tipo do arquivo (Deployment, Service).
* Metadata: Descreve algum objeto.
* Replicas: Número de réplicas.
* Containers: Definir especificações do container.

Arquivo .yaml para o deployment:

```shell script
apiVersion: apps/v1
kind: Deployment
metadata:
  name: flask-app-depoyment
spec:
  replicas: 4
  selector:
    matchLabels:
      app: flask-app
  template:
    metadata:
      labels:
        app: flask-app
    spec:
      containers:
        - name: flask    
          image: matheusbattisti/flask-kub-projeto
```

Executar Deployment:

```shell script
kubectl apply -f flask.yaml
```

Parando o deployment:

```shell script
kubectl delete -f .\flask.yaml
```

Arquivo .yaml para o service:

```shell script
apiVersion: v1
kind: Service
metadata:
  name: flask-service
spec:
  selector:
    app: flask-app
  ports:
    - protocol: 'TCP'
      port: 5000
      targetPort: 5000
  type: LoadBalancer
```

Como rodar o service:

```shell script
kubectl apply -f flask-service.yaml
```

Parar serviço:

```shell script
kubectl delete -f flask-service.yaml
```
