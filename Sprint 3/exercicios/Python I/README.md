## Exercícios parte I

**Questão 1**

Desenvolva um código em Python que crie variáveis para armazenar o nome e a idade de uma pessoa, juntamente com seus valores correspondentes. Como saída, imprima o ano em que a pessoa completará 100 anos de idade.

```python
nome = 'Daniel'
idade = 19
ano_atual = 2024

ano_buscado = ano_atual + (100 - idade)

print(ano_buscado)
```
**Questão 2**

Escreva um código Python que use a função range() para adicionar três números em uma lista(Esta lista deve chamar-se 'números')  e verificar se esses três números são pares ou ímpares. Para cada número, imprima como saída Par: ou Ímpar: e o número correspondente (um linha para cada número lido).


Importante: Aplique a função range() em seu código.

Exemplos de saída:

Par: 2
Ímpar: 3


```python
numeros = []

for numero in range(3):
    numeros.append(numero)
    if numero % 2 == 0:
        print(f'Par: {numero}')
    else:
        print(f'Ímpar: {numero}')
```

**Questão 3**

Escreva um código Python para imprimir os números pares de 0 até 20 (incluso).


Importante: Aplique a função range() em seu código.

```python
for numero in range(21):
    if numero % 2 == 0:
        print(numero)
```

**Questão 4**

Escreva um código Python para imprimir todos os números primos entre 1 até 100. Lembre-se que você deverá desenvolver o cálculo que identifica se um número é primo ou não.

Importante: Aplique a função range().

```python
for numero_testado in range(2, 101):
    for numero_escolhido in range(2, 101):
        if numero_testado % numero_escolhido == 0 \
            and numero_testado != numero_escolhido:
            break
    else:
        print(numero_testado)   
```

**Questão 5**

Escreva um código Python que declara 3 variáveis:



* dia, inicializada com valor 22

* mes, inicializada com valor 10 e

* ano, inicializada com valor 2022

Como saída, você deverá imprimir a data correspondente, no formato a seguir dia/mes/ano.

```python
dia = 22
mes = 10
ano = 2022

print(f'{dia}/{mes}/{ano}')
```

**Questão 6**

Considere as duas listas abaixo:



a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

Escreva um programa para avaliar o que ambas as listas têm em comum (sem repetições), imprimindo a lista de valores da interseção na saída padrão.

Importante:  Esperamos que você utilize o construtor set() em seu código.

```python
a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

c  = list(set(a).intersection(set(b)))
print(c)
```

**Questão 7**

Dada a seguinte lista:

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

Faça um programa que gere uma nova lista contendo apenas números ímpares.

```python
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

b = [numero for numero in a if numero % 2 != 0]

print(b)
```

**Questão 8**

Verifique se cada uma das palavras da lista ['maça', 'arara', 'audio', 'radio', 'radar', 'moto'] é ou não um palíndromo.

Obs: Palíndromo é uma palavra que permanece igual se lida de traz pra frente.



É necessário que você imprima no console exatamente assim:



* A palavra: maça não é um palíndromo
 
* A palavra: arara é um palíndromo
 
* A palavra: audio não é um palíndromo
 
* A palavra: radio não é um palíndromo
 
* A palavra: radar é um palíndromo
 
* A palavra: moto não é um palíndromo

```python
palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for palavra in palavras:
    if palavra[::-1] == palavra:
        print(f'A palavra: {palavra} é um palíndromo')
    else:
        print(f'A palavra: {palavra} não é um palíndromo')
```

**Questão 9**

Dada as listas a seguir:



* primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
* sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
* idades = [19, 28, 25, 31]


Faça um programa que imprima o dados na seguinte estrutura: "índice - primeiroNome sobreNome está com idade anos".



Exemplo:

0 - João Soares está com 19 anos

```python
primeirosNomes = ['Joao', 'Douglas', 'Lucas', 'José']
sobreNomes = ['Soares', 'Souza', 'Silveira', 'Pedreira']
idades = [19, 28, 25, 31]


for indice, primeiroNome in enumerate(primeirosNomes):
    print(f'{indice} - {primeiroNome} {sobreNomes[indice]} está com {idades[indice]} anos')
```

**Questão 10**

Escreva uma função que recebe uma lista e retorna uma nova lista sem elementos duplicados. Utilize a lista a seguir para testar sua função.



['abc', 'abc', 'abc', '123', 'abc', '123', '123']

```python
def remove_duplicatas(lista):
    lista_sem_duplicatas = list(set(lista))
    return lista_sem_duplicatas

lista  = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
print(remove_duplicatas(lista))
```

**Questão 11**

Leia o arquivo person.json, faça o parsing e imprima seu conteúdo.

Dica: leia a documentação do pacote json

```python
import json

with open('person.json', 'r') as pessoa:
    dados = json.load(pessoa)
    print(dados)
```

**Questão 12**

Implemente a função my_map(list, f) que recebe uma lista como primeiro argumento e uma função como segundo argumento. Esta função aplica a função recebida para cada elemento da lista recebida e retorna o resultado em uma nova lista.


Teste sua função com a lista de entrada [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] e com uma função que potência de 2 para cada elemento.

```python
def my_map(lista, f):
    nova_lista = list(map(f, lista))
    return nova_lista

def quadrados(x):
    return x ** 2

minha_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_map(minha_lista, quadrados))
```

**Questão 13**

Escreva um programa que lê o conteúdo do arquivo texto arquivo_texto.txt e imprime o seu conteúdo.

Dica: leia a documentação da função open(...)

```python
with open('arquivo_texto.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha, end="")
```

**Questão 14**

Escreva uma função que recebe um número variável de parâmetros não nomeados e um número variado de parâmetros nomeados e imprime o valor de cada parâmetro recebido.

Teste sua função com os seguintes parâmetros:

(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)

```python
def funcao(*args, **args_nomeados):
    for arg in args:
        print(arg)
    for chave, valor in args_nomeados.items():
        print(valor)
        

funcao(1, 3, 4, 'hello', parametro_nomeado='alguma coisa', x=20)
```

**Questão 15**

Implemente a classe Lampada. A classe Lâmpada recebe um booleano no seu construtor, Truese a lâmpada estiver ligada, False caso esteja desligada. A classe Lampada possuí os seguintes métodos:

liga(): muda o estado da lâmpada para ligada

desliga(): muda o estado da lâmpada para desligada

esta_ligada(): retorna verdadeiro se a lâmpada estiver ligada, falso caso contrário

Para testar sua classe:

1. Ligue a Lampada

2. Imprima: A lâmpada está ligada? True

3. Desligue a Lampada

4. Imprima: A lâmpada ainda está ligada? False

```python
class Lampada:
    def __init__(self, ligada):
        self.ligada = ligada
    
    def liga(self):
        self.ligada = True
        
    def desliga(self):
        self.ligada = False
        
    def esta_ligada(self):
        return self.ligada
        

lampada = Lampada(True)
print(lampada.esta_ligada())
lampada.desliga()
print(lampada.esta_ligada())
```

**Questão 16**

Escreva uma função que recebe uma string de números separados por vírgula e retorne a soma de todos eles. Depois imprima a soma dos valores.

A string deve ter valor  "1,3,4,6,10,76"

```python
def imprimi_soma(numeros):
    soma = 0
    numeros = numeros.split(',')
    for numero in numeros:
        soma += int(numero)
    return soma
    
print(imprimi_soma("1,3,4,6,10,76"))
```

**Questão 17**

Escreva uma função que recebe como parâmetro uma lista e retorna 3 listas: a lista recebida dividida em 3 partes iguais. Teste sua implementação com a lista abaixo


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

```python
def retorna_listas(lista):
   tamanho_listas = int(len(lista) / 3)
   return f'{lista[:tamanho_listas]} {lista[tamanho_listas : 2 * tamanho_listas]} {lista[2 * tamanho_listas : 3 * tamanho_listas]}'
   
   
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] 
print(retorna_listas(lista))
```

**Questão 18**

Dado o dicionário a seguir:

speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}

Crie uma lista com todos os valores (não as chaves!) e coloque numa lista de forma que não haja valores duplicados.

```python
def remove_duplicatas(dicionario):
    lista = []
    for valor in dicionario.values():
            lista.append(valor)
    print(list(set(lista)))
    
    
speed = {'jan':47, 'feb':52, 'march':47, 'April':44, 'May':52, 'June':53, 'july':54, 'Aug':44, 'Sept':54}
remove_duplicatas(speed)
```

**Questão 19**

Calcule o valor mínimo, valor máximo, valor médio e a mediana da lista gerada na célula abaixo:



Obs.: Lembrem-se, para calcular a mediana a lista deve estar ordenada!



import random 

amostra aleatoriamente 50 números do intervalo 0...500

random_list = random.sample(range(500),50)


Use as variáveis abaixo para representar cada operação matemática:



mediana
media
valor_minimo 
valor_maximo 


Importante: Esperamos que você utilize as funções abaixo em seu código:

* random

* max

* min

* sum

```python
import random

random_list = sorted(random.sample(range(500), 51))

elemento_central = len(random_list) // 2 - 1 if len(random_list) % 2 == 0 else len(random_list) // 2 
mediana = random_list[elemento_central]
media = sum(random_list)/ len(random_list)
valor_minimo = min(random_list)
valor_maximo = max(random_list)

print(f'Media: {media}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}')
```

**Questão 20**

Imprima a lista abaixo de trás para frente.

a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]

```python
a = [1, 0, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(a[::-1])
```

**Questão 21**

Implemente duas classes, Pato e Pardal , que herdam de uma superclasse chamada Passaro as habilidades de voar e emitir som.



Contudo, tanto Pato quanto Pardal devem emitir sons diferentes (de maneira escrita) no console, conforme o modelo a seguir.



Imprima no console exatamente assim:

Pato

Voando...

Pato emitindo som...

Quack Quack

Pardal

Voando...

Pardal emitindo som...

Piu Piu

```python
class Passaro:
    def __init__(self, nome, som):
        self.nome = nome
        self.som = som
        
    def voar(self):
        print(self.nome)
        print('Voando')
    
    def emitir_som(self):
        print(f'{self.nome} emitindo som...')
        print(self.som)
        
    

class Pato(Passaro):
    def __init__(self, nome, som):
        super().__init__(nome, som)
        
class Pardal(Passaro):
    def __init__(self, nome, som):
        super().__init__(nome, som)
        

pato = Pato('Pato', 'Quack Quack')
pardal = Pardal('Pardal', 'Piu Piu')

pato.voar()
pato.emitir_som()

pardal.voar()
pardal.emitir_som()
```

**Questão 22**

Crie uma classe chamada Pessoa, com um atributo privado chamado nome (declarado internamente na classe como __nome) e um atributo público de nome id.

Adicione dois métodos à classe, sendo um para definir o valor de __nome e outro para retornar o valor do respectivo atributo.

Lembre-se que o acesso ao atributo privado deve ocorrer somente através dos métodos definidos, nunca diretamente.  Você pode alcançar este comportamento através do recurso de properties do Python.



Veja um exemplo de como seu atributo privado pode ser lido e escrito:



pessoa = Pessoa(0) 

pessoa.nome = 'Fulano De Tal'

print(pessoa.nome)

```python
class Pessoa:
    def __init__(self, id):
        self.id = id
        self.__nome = None

    def set_nome(self, nome):
        self.__nome = nome
    
    def get_nome(self):
        return self.__nome
    
    nome = property(
        get_nome,
        set_nome
    )

pessoa = Pessoa(0)
pessoa.nome = 'Daniel'
print(pessoa.nome)
```

**Questão 23**

Crie uma classe  Calculo  que contenha um método que aceita dois parâmetros, X e Y, e retorne a soma dos dois. Nessa mesma classe, implemente um método de subtração, que aceita dois parâmetros, X e Y, e retorne a subtração dos dois (resultados negativos são permitidos).

```python
class Calculo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def subtracao(self):
        return self.x - self.y
    
    def soma(self):
        return self.x + self.y
        
        
calculo = Calculo(4, 5)

print(f'Somando: {calculo.x} + {calculo.y} : {calculo.soma()}')
print(f'Subtraindo: {calculo.x} - {calculo.y} : {calculo.subtracao()}')
```

**Questão 24**

Crie uma classe Ordenadora que contenha um atributo listaBaguncada e que contenha os métodos ordenacaoCrescente e ordenacaoDecrescente.

Instancie um objeto chamado crescente dessa classe Ordenadora que tenha como listaBaguncada a lista [3,4,2,1,5] e instancie um outro objeto, decrescente dessa mesma classe com uma outra listaBaguncada sendo [9,7,6,8].

Para o primeiro objeto citado, use o método ordenacaoCrescente e para o segundo objeto, use o método ordenacaoDecrescente.



Imprima o resultado da ordenação crescente e da ordenação decresce

[1, 2, 3, 4, 5] 
[9, 8, 7, 6]

```python
class Ordenadora:
    def __init__(self, listaBaguncada):
        self.listaBaguncada = listaBaguncada

    
    def ordenacaoCrescente(self):
        self.listaBaguncada = sorted(self.listaBaguncada)
        return self.listaBaguncada

    
    def ordenacaoDecrescente(self):
        self.listaBaguncada = sorted(self.listaBaguncada)
        self.listaBaguncada = self.listaBaguncada[::-1]
        return self.listaBaguncada


crescente = Ordenadora([3,4,2,1,5])
decrescente = Ordenadora([9,7,6,8])

print(crescente.ordenacaoCrescente())
print(decrescente.ordenacaoDecrescente())
```

**Questão 25**

Crie uma classe Avião que possua os atributos modelo, velocidade_maxima, cor e capacidade.

Defina o atributo cor de sua classe , de maneira que todas as instâncias de sua classe avião sejam da cor “azul”.

Após isso, a partir de entradas abaixo, instancie e armazene em uma lista 3 objetos da classe Avião.

Ao final, itere pela lista imprimindo cada um dos objetos no seguinte formato:

“O avião de modelo “x” possui uma velocidade máxima de “y”, capacidade para “z” passageiros e é da cor “w”.

Sendo x, y, z e w cada um dos atributos da classe “Avião”.



Valores de entrada:

* modelo BOIENG456: velocidade máxima 1500 km/h: capacidade para 400 passageiros: Cor Azul

* modelo Embraer Praetor 600: velocidade máxima 863km/h: capacidade para 14 passageiros: Cor Azul

* modelo Antonov An-2: velocidade máxima de 258 Km/h: capacidade para 12 passageiros: Cor Azul

```python
class Aviao:
    cor = 'Azul'
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade


lista = [Aviao('BOIENG456', '1500 km/h', 400), Aviao('Embraer Praetor 600', '863km/h', 14), Aviao('Antonov An-2', '258 Km/h', 12)]

for aviao in lista:
    print(f'O avião de modelo {aviao.modelo} possui uma velocidade máxima de {aviao.velocidade_maxima}, capacidade para {aviao.capacidade} passageiros e é da cor {aviao.cor}.')
```