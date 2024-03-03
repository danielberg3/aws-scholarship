# Linux

O ambiente linux é uma ferramenta essencial na vida do desenvolvedor, dado que este é muito utilizado por empresas na hora de construção dos servidores, pois além da facilidade que ele possibilita também é uma ferramenta gratuita. Conhecer seus comandos traz praticidade e eficiência para aqueles que o utilizam.

## Sumário

1. [Principais comandos](#principais-comandos)
2. [Gerenciar pacotes](#gerenciar-pacotes)
3. [Busca em arquivos ou diretórios](#busca-em-arquivos-ou-diretórios)
4. [Comandos do nano](#comandos-do-nano)
5. [Comandos no Vim](#comandos-no-vim)
6. [Usuário e grupos](#usuário-e-grupos)
7. [Grupos](#grupos)
8. [Gerenciar Permissões](#gerenciar-permissões)
9. [Configuração de redes](#configuração-de-redes)
10. [Compactar e descompactar arquivos](#compactar-e-descompactar-arquivos)


## Principais comandos


**COMDANDOS CD**

1. Voltar para o último diretório em que estava trabalhando:     
    
    ```bash 
     cd -
    ```

2. Entrar na pasta de usuário:
    
    ```bash 
    cd     
    ```

3. concatenar comandos:     
    
    ```bash 
     cd pasta && ls
    ```


**COMANDOS LS**

1. Mostar arquivos detalhadamente:

    ```bash 
    ls -l
    ```

2. Apresentar arquivos ocultos:

    ```bash 
    ls -a
     ```

3. Apresentar arquivos por ordem de criação:

    ```bash 
    ls -ltr
     ```

4. Apresentar arquivos de uma forma mais humana:

    ```bash 
    ls -lh
     ```

5. Mostar arquivos em ordem reversa:

    ```bash 
    ls -lr /pasta
     ```

6. Mostar diretórios detalhadamente:

    ```bash 
    ls -R
     ```

7. Mostar arquivos ordenados por tamanho: 

    ```bash 
    ls -lS
     ```

8. Mostar opções do comando:

    ```bash 
    ls --help
     ```

**COMANDOS CAT**

1. Ler arquivo:

    ```bash 
    cat -n arquivo.txt arquivo2.txt
     ```

2. Criar arquivo com outros dois arquivos:

    ```bash 
    cat arquivo.txt arquivo2.txt > arquivo3.txt
     ```

3. Concatenar assunto de arquivo dentro do outro:

    ```bash 
    cat arquivo.txt >> arquivo2.txt
     ```

**COMANDOS TOUCH**

1. Criar arquivo / atulizar data de modificação do arquivo (quando o arquivo já foi criado):

    ```bash 
    touch arquivo.txt
     ```

**COMANDO MAN**

1. Ver manual do comando:

    ```bash 
    man <comando>
     ```

2. Ver comandos utlizados anteriormente:

    ```bash 
    CRTL + R
     ```

**COMANDO MKDIR**

1. Criar diretório:

    ```bash 
    mkdir diretorio
     ```

**COMANDO RM**

1. Remover arquivos:

    ```bash 
    rm arquivo.txt
     ```

2. Remover diretórios que não estão vazios:

    ```bash 
    rm -rfv diretorio
     ```

**COMANDO CP**

3. Copiar arquivos:

    ```bash 
    cp arquivo.txt /diretorio
     ```

4. Copiar diretórios:

    ```bash 
    cp -R ./diretorio /novo_diretorio
     ```

**COMANDO MV**

1. Mover arquivo ou diretório:

    ```bash 
    mv arquivo.txt /diretorio
     ```
    
     ```bash 
    mv ./diretorio /diretorio
     ```

**COMANDO PWD**

1. Exibe o caminho relativo no qual o usuário encontra:

    ```bash 
    pwd
     ```

# Gerenciar pacotes

**Atualizar pacotes**

1. Atualizar repositórios:

    ```bash 
    sudo apt-get update
     ```

2. Atualizar pacotes:

    ```bash 
    sudo apt-get upgrade
     ```

**Baixar pacotes**

1. Ver se o pacote está instalado:

    ```bash 
    tree
     ```

2. Instalar pacote:

    ```bash 
    sudo apt-get install tree
     ```

**Apagar pacotes**

1. Remover aplicativos:

    ```bash 
    sudo apt-get purge tree
     ```

2. Remover pacotes denecessários / não mais utilizados:

    ```bash 
    sudo apt-get autoremove
     ```

**Pesquisar pacotes**

1. Pesquisar pacotes:

    ```bash 
     ```
    apt-cache search postgres

## Busca em arquivos ou diretórios


**HEAD**


1. Ver topo de um arquivo:
    ```bash 
    head -n 1 documento.txt
     ```

2. Criar documento a partir do head de outro:

    ```bash 
    head -n 1 documento.txt > documento2.txt
     ```

**TAIL**

1. Ver fim de um arquivo:

    ```bash 
    tail -n 1 documento.txt
     ```

2. Criar documento a partir do tail de outro:

    ```bash 
    tail -n 1 documento.txt > documento2.txt
     ```

3. Acompanhar fim do arquivo em tempo de execução:

    ```bash 
    tail -f documento.txt
     ```

**GREP**

1. Pesquisar palavras dentro de arquivos:

    ```bash 
    grep -i 'PaLAvRa' documento.txt
     ```

2. Pesquisar quantidade de vezes que a palavra aparece dentro do arquivo:

    ```bash 
    grep -c 'palavra' documento.txt
     ```

3. Pesquisar palavra dentro da pasta independente do arquivo:

    ```bash 
    grep  'palavra' -r
    ```

**FIND**

1. Encontrar arquivos e diretórios:

    ```bash 
    find -iname arquivo.txt
     ```

    ```bash 
    find -iname diretorio
     ```

2. Encontrar diretórios e arquivos vazios no diretório atual respectivamente:

    ```bash 
    find -empty -type d
     ```

    ```bash 
    find -empty -type f
     ```

3. Saber pasta de origem do comando:

    ```bash 
    which <comando>
    ```

## Comandos do nano

1. Inserir arquivo dentro de outro com o nano aberto

    ```bash 
    CRTL + R
    ```

1. Manipular texto
    ```bash 
	Alt + a     # selecionar texto
	Alt + 6     # copiar conteúdo
	CRTL + k    # recortar conteúdo
	CRTL + u    # colar conteúdo
    ```


1. Fim e início do arquivo respectivamente:

    ```bash 
    Alt + /     # fim do arquivo
    Alt + \     # início do arquivo
    ```

1.  Informar a linha que deseja ir:

    ```bash 
    Alt + g
    ```

1. Buscar palavra no nano:
    ```bash 
    CRTL + w
    ```

1.  Replace:
    ```bash 
    Alt + r
    ```

## Comandos no Vim

1. Criar arquivo com vim:

    ```bash 
    vim arquivo.txt
    ```

1. Modo de inserção de comandos:
    ```bash 
    i
    ```

1. Sair do modo de inserção de comandos:

    ```bash 
    esc
    ```

1. Salvar e sair do arquivo:

    ```bash 
    :x  
    ```

1. Salvar sem sair do arquivo:
    
    ```bash 
    :w  
    ```

1. Sair do arquivo:
    
    ```bash 
    :q      
    ```

1. Deletar linha:
    ```bash 
    dd
    ```

1. Reverter o que apagou:
    ```bash 
    u
    ```

1. Reverter reversão:

    ```bash 
    CTRL + l
    ```

1. Pesquisar palavra, usar n para passar entre as palavras e shift + n para voltar:

    ```bash 
    /palavra
    ```

1. Replace em todas as ocorrências da palavra:

    ```bash 
    :%s/palavra_original/palavra_mudar/g
    ```

1. Replace na palavra da linha:

    ```bash 
    :s/palavra_original/palavra_mudar/g
    ```

1. Sair sem salvar as alterações:

    ```bash 
    :q!
    ```

## Usuário e grupos

1. Criar usuário:

    ```bash 
    sudo adduser usuario
    ```

1. Deletar usuário:

    ```bash 
    sudo userdel --remove usuario
    ```

1. Mudar nome do usuário no display:

    ```bash 
    sudo usermod -c 'Daniel' usuario
    ```

1. Modificar nome do usuário na pasta home:

    ```bash 
    sudo usermod -l usuario -d /home/usuario -m daniel
    ```


1. Bloquear um usuário:

    ```bash 
    sudo usermod -L daniel
    ```

1. Desbloquear um usuário:
    
    ```bash 
    sudo usermod -U daniel
    ```

## Grupos


1. Ver grupos criados:

    ```bash 
    getent group
    ```

1. criar grupo:

    ```bash 
    sudo groupadd -g 9999 devs 
    ```

1. Deletar grupo:

    ```bash 
    sudo groupdel devs
    ```

1. Ver grupo do usuário:

    ```bash 
    groups daniel
    ```

1. Adicionar a novo grupo:

    ```bash 
    sudo usermod -a -G devs daniel
    ```

1. Remover usuário de grupo:

    ```bash 
    sudo gpasswd -d daniel devs
    ```

1. virar um super usuário:

    ```bash 
    sudo su
    ```

1. trocar senha de usuário:

    ```bash 
    passwd
    ```

## Gerenciar Permissões

```bash 
# 1 (arquivo ou diretório) 
# 222 (permissões do dono) 
# 333 (permissões do grupo) 
# 444 (permissões de outros usuários)

# - : arquivo
# d : diretório
# r : ler
# w : escrever
# x : executar

# exemplo: -rwx-rw--r--
```

1. Mudar permissão numérica:
    ```bash
    Valor | Permissões
    ------+-----------
    0     | ---
    1     | --x
    2     | -w-
    3     | -wx
    4     | r--
    5     | r-x
    6     | rw-
    7     | rwx

    ```

    ```bash 
    chmod 444 arquivo.txt
    ```

1. Mudar permissção simbólica:

    ```bash 
    # + : adicionar permissão
    # - : remover permissão
    # = : substituir permissões por uma nova

    # a : todos os usuários
    # o : outros usuários
    # u : usuário dono
    # g : grupo
    ```

    ```bash 
    chmod o-r arquivo.txt
    ```

1. Mudar arquivo/pasta de dono:

    ```bash 
    sudo chown daniel arquivo.txt
    ```
1. Mudar arquivo/pasta de dono e grupo:

    ```bash 
    sudo chown devs:daniel arquivo.tx
    ```


OBS.: mesmo que o dono do arquivo esteja em um grupo com permissões sobre o arquivo, se ele não tem permissões não poderá fazer nada.

5. Mudar aquivo/pasta de apenas de grupo:

    ```bash 
    chgrp dankiles arquivo.txt
    ```

1. Ver o histórico de comandos digitados:
    
    ```bash 
	history
    ```

## Configuração de redes

1. Comandos para ver se a conexão está funcionando:

    ```bash 
    ping google.com
    ping 8.8.8.8
    ```

1. Verficar conexões que estão sendo feitas:

    ```bash 
    netstat
    ```

1. Verficar conexões TCP que estão sendo feitas:

    ```bash 
    netstat -at
    ```

1. Verficar conexões UDP que estão sendo feitas:

    ```bash 
    netstat -au
    ```

1. Abrir conexão udp com google na porta 80:

    ```bash 
    netcat -u google.com 80
    ```

1. Ver informações sobre as interfaces de rede:

    ```bash 
    ifconfig
    ```

1. Ver ip do servidor através de seu dns:

    ```bash 
    nslookup google.com
    ```

1. Ver conexões TCP que estão ocorrendo:
    ```bash 
    sudo tcpdump
    ```

1. Verificar IP de conexão da nossa máquina:
    ```bash 
    hostname -I
    ```

## Compactar e descompactar arquivos


1. Compactar arquivo:

    ```bash 
    tar -czvf compactado.tar.gz diretorio
    ```

1. Compactar vários arquivos de uma vez só:

    ```bash 
    tar -czvf compactado.tar.gz diretorio arquivo.txt arquivo2.txt
    ```

1. Descompactar arquivo:

    ```bash 
    tar -xzvf compactado.tar.gz -C descompactar/
    ```

1. Compactar como zip:

    ```bash 
    zip -r compactado.zip diretorio
    ```

1. Descompactar zip:

    ```bash 
    unzip compactado3.zip -d /caminho
    ```

1. Ver o que tem dentro do tar:

    ```bash 
    tar -tvf compactado2.tar.gz
    ```