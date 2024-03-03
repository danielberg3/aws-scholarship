# GIT & GITHUB

A utilização do git e github é uma ótima prática na hora de se construir projetos. Isso porque a combinação das ferramentas permite que desenvolvedores guardem as versões de seus projetos e dividam seus ambientes de trabalho. Assim, em casos de conflitos de código ou corrupção de arquivos, basta apenas voltar para uma versão que funcione ou gerenciar diferentes ramos de um projeto para que se unam corretamente.


## Sumário

1. [Principais comandos GIT](#principais-comandos-git)
2. [Branches](#branches)
3. [Branches compartilhadas](#branches-compartilhadas)
4. [Análise e inspeção de repositórios](#análise-e-inspeção-de-repositórios)
5. [Administração do repositório](#administração-do-repositório)
6. [Melhorando os commits](#melhorando-os-commits)


## Principais comandos GIT

1. Iniciar repositório git:

    ```bash
    git init
    ```
1. Ver mudanças no projeto:

    ```bash
    git status
    ```
1. Adicionar mudanças para o commit:

    ```bash
    git add .
    ```
1. Fazer o commit de arquivos:

    ```bash
    git commit -m "initial commit"
    ```
1. Enviar alterações para o repositório remoto:

    ```bash
    git push
    ```
1. Puxar alterações do repositório remoto para o local:

    ```bash
    git pull
    ```
1. Fazer um clone do repositório:

    ```bash
    git clone git@github.com:danielberg3/demo.git
    ```
1. Remover arquivo do git:

    ```bash
    git rm arquivo.txt
    ```
1. Ver informações sobre os commits já realizados:

    ```bash
    git log
    ```
1. Mudar nome de arquivo com git:

    ```bash
    git mv arquivo.css file.css
    ```
1. Mover arquivo:

    ```bash
    git mv arquivo.css css/arquivo.css
    ```
1. Remover alterações do arquivo voltando ao estado da main remota:

    ```bash
    git checkout css/arquivo.css
    ```
1. Remover alterações bem como commits que ainda não foram enviados para o repositório remoto:

    ```bash
    git reset --hard origin/main
    ```
.gitignore: arquivo no qual é informado os diretórios e arquivos a serem ignorados pelo git.

## Branches

São ramificações do projeto, ou espaços de trabalho para cada um dos desenvolvedores, os quais são unidos a main no fim para adição de novas funcionalidades.

1. Ver as branches existentes:

    ```bash
    git branch
    ```
1. Criar branch (o ideal é sempre criar a partir da main):

    ```bash
    git branch nova_branch
    ```
1. Deletar branch (apenas se for extremamente necessário):

    ```bash
    git branch -d nova_branch
    ```
1. Mudar de branch:

    ```bash
    git checkout nova_branch
    ```
1. Criar branch e mudar para ela:

    ```bash
    git checkout -b nova_branch
    ```
1. Unir branch atual com outra branch:

    ```bash
    git merge main
    ```
1. Enviar alterações que ainda não sofreram o commit para a lixeira:

    ```bash
    git stash
    ```
1. Ver lista de stash:

    ```bash
    git stash list
    ```
1. Ver o que tem dentro de uma stash:

    ```bash
    git stash show -p 3
    ```
1. Adicionar o conteúdo da stash novamente no código:

    ```bash
    git stash apply 3
    ```
1. Remover stash específica:

    ```bash
    git stash drop 3
    ```
1. Remover todas as stash da branch:

    ```bash
    git stash clear
    ```
1. Criar tag (versão de uma branch):

    ```bash
    git tag -a v1.0  -m "primeira versão"
    ```
1. Ver tags existentes:

    ```bash
    git tag
    ```
1. Ver conteúdo da tag:

    ```bash
    git show v1.0
    ```
1. Mudar de tag:

    ```bash
    git checkout v1.0
    ```
1. Enviar uma tag para o repositório remoto:

    ```bash
    git push origin v1.0
    ```
1. Enviar todas as tags para o repositório remoto:

    ```bash
    git push origin --tags
    ```
## Branches compartilhadas

1. Mapear branches compartilhadas no repositório remoto:

    ```bash
    git fetch -a
    ```
1. Mudar para uma das branches locais:

    ```bash
    git checkout minhaBranch
    ```
1. Puxar alterações do repositório remoto:

    ```bash
    git pull
    ```
1. Enviar alterações do repositório local para o remoto:

    ```bash
    git push
    ```
1. Ver URLs do repositório remoto:

    ```bash
    git remote -v
    ```
1. Remover URLs do repositório remoto:

    ```bash
    git remote rm origin
    ```
1. Adicionar URLs do repositório remoto:

    ```bash
    git remote add origin git@github.com:danielberg3/demo.git
    ```
1. Adicionar submódulo:

    ```bash
    git submodule add git@github.com:danielberg3/newdemo.git submodulo
    ```
1. Ver submódulos de um projeto:

    ```bash
    git submodule
    ```
1. Enviar alterações da forma correta para o submódulo:

    ```bash
    git push --recurse-submodules=on-demand
    ```
## Análise e inspeção de repositórios

1. Ver movimentação do branch ou tag:

    ```bash
    git show
    ```
1. Ver diferenças entre branch local e remota:

    ```bash
    git diff
    ```
1. Ver diferenças entre arquivo remoto e local:

    ```bash
    git diff HEAD:arquivo.txt arquivo.txt
    ```
1. Receber log resumido sobre o projeto:

    ```bash
    git shortlog
    ```
## Administração do repositório

1. Remover arquivos do untracked:

    ```bash
    git clean -f
    ```
1. Identificar arquivos que não são mais necessários e excluí-los:

    ```bash
    git gc
    ```
1. Verificar a integridade dos arquivos:

    ```bash
    git fsck
    ```
1. Ver os passos do desenvolvedor dentro do repositório:

    ```bash
    git reflog
    ```
1. Voltar ou passar para um dos passos do reflog:

    ```bash
    git reset --hard 8e776a2
    ```
1. Gerar arquivo zip a partir do repositório:

    ```bash
    git archive  --format zip --output arquivos_main.zip main
    ```
## Melhorando os commits

1. Selecionar e alterar o commits que devem ser enviados para uma nova branch:
    
    ```bash
    git rebase func_a private_func_a -i

    # pick: commit a ser enviado.
    # squash: commit a ser ignorado.
    # reword: commit a ser renomeado.
    ```