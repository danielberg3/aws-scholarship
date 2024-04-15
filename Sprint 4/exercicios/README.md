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

# Exercícios

<!-- #region -->
**E01**

Você está recebendo um arquivo contendo 10.000 números inteiros, um em cada linha. Utilizando lambdas e high order functions, apresente os 5 maiores valores pares e a soma destes.



Você deverá aplicar as seguintes funções no exercício:



* map
 
* filter
 
* sorted
 
* sum



Seu código deverá exibir na saída (simplesmente utilizando 2 comandos `print()`):



* a lista dos 5 maiores números pares em ordem decrescente;

* a soma destes valores.
<!-- #endregion -->

```python
def inteiros(n):
    return int(n)


arquivo = open('number.txt', 'r')
numeros = arquivo.readlines()
numeros = map(inteiros, numeros)
numeros = filter(lambda x: x % 2 == 0, numeros)

ordenados = sorted(numeros)[::-1]

print(ordenados[:5])
print(sum(ordenados[:5]))

```

<!-- #region -->
**E02**

Utilizando high order functions, implemente o corpo da função conta_vogais. O parâmetro de entrada será uma string e o resultado deverá ser a contagem de vogais presentes em seu conteúdo.



É obrigatório aplicar as seguintes funções:

* len

* filter

* lambda



Desconsidere os caracteres acentuados. Eles não serão utilizados nos testes do seu código.
<!-- #endregion -->

```python
def conta_vogais(texto):
    vogais = list(filter(lambda letra: letra.lower() in ('a', 'e', 'i', 'o', 'u') , texto))
    return len(vogais)
```

<!-- #region -->
**E03**

A função calcula_saldo recebe uma lista de tuplas, correspondendo a um conjunto de lançamentos bancários. Cada lançamento é composto pelo seu valor (sempre positivo) e pelo seu tipo (C - crédito ou D - débito). 

Abaixo apresentando uma possível entrada para a função.



lancamentos = [
    (200,'D'),
    (300,'C'),
    (100,'C')
]


A partir dos lançamentos, a função deve calcular o valor final, somando créditos e subtraindo débitos. Na lista anterior, por exemplo, teríamos como resultado final 200.



Além de utilizar lambdas, você deverá aplicar, obrigatoriamente, as seguintes funções na resolução:



* reduce (módulo functools)

* map
<!-- #endregion -->

```python
from functools import reduce


def calcula_saldo(lancamentos):
    valor_final = reduce(
        lambda acumulador, transacao: acumulador + transacao,
        map(lambda lancamento: lancamento[0] if lancamento[1] == 'C' else -lancamento[0], lancamentos),
        0
    )
    return valor_final
        
```

<!-- #region -->
**E04**

A função calcular_valor_maximo deve receber dois parâmetros, chamados de operadores e operandos. Em operadores, espera-se uma lista de caracteres que representam as operações matemáticas suportadas (+, -, /, *, %), as quais devem ser aplicadas à lista de operadores nas respectivas posições. Após aplicar cada operação ao respectivo par de operandos, a função deverá retornar o maior valor dentre eles.



Veja o exemplo:



* Entrada

operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]


* Aplicar as operações aos pares de operandos

[ 3+6 , -7-4.9, 8*-8 , 10/2 , 8+4 ] 


* Obter o maior dos valores

12


Na resolução da atividade você deverá aplicar as seguintes funções:

* max

* zip

* map
<!-- #endregion -->

```python
from itertools import cycle

def calcular_valor_maximo(operadores,operandos):
    equacoes = zip(cycle(operadores), operandos)
    maior = max(map(lambda linha: eval(f'{linha[1][0]} {linha[0]} {linha[1][1]}'), equacoes))
    return maior
    
```

<!-- #region -->
**E05**

Um determinado sistema escolar exporta a grade de notas dos estudantes em formato CSV. Cada linha do arquivo corresponde ao nome do estudante, acompanhado de 5 notas de avaliação, no intervalo [0-10]. É o arquivo estudantes.csv de seu exercício.



Precisamos processar seu conteúdo, de modo a gerar como saída um relatório em formato textual contendo as seguintes informações:



* Nome do estudante

* Três maiores notas, em ordem decrescente

* Média das três maiores notas, com duas casas decimais de precisão

O resultado do processamento deve ser escrito na saída padrão (print), ordenado pelo nome do estudante e obedecendo ao formato descrito a seguir:



Nome: <nome estudante> Notas: [n1, n2, n3] Média: <média>



Exemplo:

Nome: Maria Luiza Correia Notas: [7, 5, 5] Média: 5.67

Nome: Maria Mendes Notas: [7, 3, 3] Média: 4.33



Em seu desenvolvimento você deverá utilizar lambdas e as seguintes funções:

* round

* map

* sorted
<!-- #endregion -->

```python
def processa_conteudo(string):
    estudante = string.strip('\n').split(',')
    estudante[1:] = [int(x) for x in estudante[1:]]
    
    menor_nota = min(estudante[1:])
    estudante.remove(menor_nota)
    
    menor_nota = min(estudante[1:])
    estudante.remove(menor_nota)
    
    media_notas = round(sum(estudante[1:])/3, 2)
    notas = sorted(estudante[1:])[::-1]
    
    estudante_atualizado = [estudante[0], notas, media_notas]
    
    return estudante_atualizado


with open('estudantes.csv', 'r') as arquivo:
    estudantes = map(processa_conteudo, arquivo)
    estudantes = sorted(estudantes, key=lambda linha: linha[0])
    
    for estudante in estudantes:
        print(f'Nome: {estudante[0]} Notas: {estudante[1]} Média: {estudante[2]}')
    
```

<!-- #region -->
**E06**

Você foi encarregado de desenvolver uma nova feature  para um sistema de gestão de supermercados. O analista responsável descreveu o requisito funcional da seguinte forma:



- Para realizar um cálculo de custo, o sistema deverá permitir filtrar um determinado conjunto de produtos, de modo que apenas aqueles cujo valor unitário for superior à média deverão estar presentes no resultado. Vejamos o exemplo:



Conjunto de produtos (entrada):



* Arroz: 4.99

* Feijão: 3.49
 
* Macarrão: 2.99
 
* Leite: 3.29
 
* Pão: 1.99



Produtos com valor acima da média:

* Arroz: 4.99

* Feijão: 3.49





Observe que estamos definindo a assinatura de uma função como parte de sua resposta. Você não pode mudá-la, apenas codificar seu corpo. O parâmetro conteudo é um dicionário cuja chave contém o nome do produto e o valor, o respectivo preço (ponto flutuante).

Observe um exemplo de valor para conteudo:



{
    "arroz": 4.99,
    "feijão": 3.49,
    "macarrão": 2.99,
    "leite": 3.29,
    "pão": 1.99
}
O retorno da função obrigatoriamente deve ser uma lista. Cada elemento da lista é uma tupla em que a primeira posição contém o nome do produto e a segunda, o respectivo preço. Veja um exemplo de retorno:



[
 
('feijão', 3.49),
 
 ('arroz', 4.99)
 
]


Importante: O retorno da função deve estar ordenado pelo preço do item (ordem crescente).


<!-- #endregion -->

```python
def maiores_que_media(conteudo):
    media = sum(conteudo.values()) / len(conteudo)
    produtos = filter(lambda produto: produto[1] > media, conteudo.items())
    produtos = sorted(produtos, key=lambda linha: linha[1])
    return produtos
    
```

**E07**

Generators são poderosos recursos da linguagem Python. Neste exercício, você deverá criar o corpo de uma função, cuja assinatura já consta em seu arquivo de início (def pares_ate(n:int):) .

O objetivo da função pares_ate é retornar um generator para os valores pares no intervalo [2,n] . Observe que n representa o valor do parâmetro informado na chamada da função.

```python
def pares_ate(n):
    par = 0
    while par < n:
        par += 2
        yield par
                
```
