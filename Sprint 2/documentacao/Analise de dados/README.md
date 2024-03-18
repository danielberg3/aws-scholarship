# SQL para Análise de Dados: Do básico ao avançado

O processo de armazenamento de dados ocorre já a bastante tempo, seja através de planinhas ou ficheiros, porém o gerenciamento desses dados nas ferramentas citadas não se torna tão prático, pois, a construção de informações, ou seja, a verificação de como diferentes dados se comunicam, fica praticamente impossível de ser feita por humanos. 

Assim, surgem os SGBD's, que permitem contultas sobre grandes volumes de dados com o objetivo de gerar relatórios valiosos. Sendo profissional analista de dados o responsável por construir as famosas queries para consulta.

## Sumário

1. [Comandos Básicos](#comandos-básicos)
2. [Operadores](#operadores)
3. [Funções Agregadas](#funções-agregadas)
4. [Joins](#joins)
5. [Union](#union)
6. [Subqueries](#subqueries)
7. [Tratamento de Dados](#tratamento-de-dados)
8. [Manipulação de Tabelas](#manipulação-de-tabelas)

## Comandos Básicos

SELECT

```sql
-- Serve para selecionar colunas de tabelas

select coluna_1, coluna_2, coluna_3
from schema_1.tabela_1
```

DISTINCT

```sql
-- Serve para remover linhas duplicadas e mostrar apenas linhas distintas
-- Muito usado na etapa de exploração das bases 

select distinct coluna_1, coluna_2, coluna_3
from schema_1.tabela_1
```

WHERE

```sql
-- Serve para filtrar linhas de acordo com uma condição

select coluna_1, coluna_2, coluna_3
from schema_1.tabela_1
where condição_x=true
```

ORDER BY

```sql
-- Serve para ordenar a seleção de acordo com uma regra definida pelo usuário

select coluna_1, coluna_2, coluna_3
from schema_1.tabela_1
where condição_x=true
order by coluna_1
```

LIMIT

```sql
-- Serve para limitar o nº de linhas da consulta.
-- Muito utilizado na etapa de exploração dos dados

select coluna_1, coluna_2, coluna_3
from schema_1.tabela_1
limit N
```

## Operadores

OPERADORES ARITMÉTICOS

```sql
-- Usados para unir expressões simples em uma composta

-- +
-- -
-- *
-- /
-- ^
-- %
-- || --> não é um operador aritmético

-- (Exemplo 1) Criação de coluna calculada
-- Crie uma coluna contendo a idade do cliente da tabela sales.customers

select
    email,
    birth_date,
    (current_date - birth_date) / 365 as "idade do cliente"
from sales.customers

-- (Exemplo 2) Utilização da coluna calculada nas queries
-- Liste os 10 clientes mais novos da tabela customers

select
    email,
    birth_date,
    (current_date - birth_date) / 365 as "idade do cliente"
from sales.customers
order by "idade do cliente"


-- (Exemplo 3) Criação de coluna calculada com strings 
-- Crie a coluna "nome_completo" contendo o nome completo do cliente

select
    first_name || ' ' || last_name as nome_completo
from sales.customers
```

OPERADORES DE COMPARAÇÃO

```sql
-- Servem para comparar dois valores retornando TRUE ou FALSE
-- Muito utilizado em conjunto com a função WHERE para filtrar linhas de uma seleção

-- =
-- >
-- <
-- >=
-- <=
-- <>

-- (Exemplo 1) Uso de operadores como flag
-- Crie uma coluna que retorne TRUE sempre que um cliente for um profissional clt 

select first_name,
    professional_status,
    (professional_status = 'clt') as "Cliente CLT"
    from sales.customers c 
```

OPERADORES LÓGICOS

```sql
-- Usados para unir expressões simples em uma composta

-- AND
-- OR
-- NOT
-- BETWEEN
-- IN
-- LIKE
-- ILIKE
-- IS NULL


-- (Exemplo 1) Uso do comando BETWEEN 
-- Selecione veículos que custam entre 100k e 200k na tabela products

select *
from sales.products
where price >= 100000 and price <= 200000;

select *
from sales.products p 
where price between 100000 and 200000;


-- (Exemplo 2)  Uso do comando NOT
-- Selecione veículos que custam abaixo de 100k ou acima 200k 

select *
from sales.products
where price < 100000 or price > 200000;

select *
from sales.products p 
where price not between 100000 and 200000;


-- (Exemplo 3) Uso do comando IN
-- Selecionar produtos que sejam da marca HONDA, TOYOTA ou RENAULT

select *
from sales.products
where brand = 'HONDA' or brand = 'TOYOTA' or brand = 'RENAULT';

select *
from sales.products p 
where brand in ('HONDA', 'TOYOTA', 'RENAULT');


-- (Exemplo 4) Uso do comando LIKE (matchs imperfeitos)
-- Selecione os primeiros nomes distintos da tabela customers que começam
-- com as iniciais ANA

select distinct first_name
from sales.customers
where first_name = 'ANA';

select distinct first_name 
from sales.customers c 
where first_name like 'ANA%';

select distinct first_name 
from sales.customers c 
where first_name like '%ANA';

-- (Exemplo 5) Uso do comando ILIKE (ignora letras maiúsculas e minúsculas)
-- Selecione os primeiros nomes distintos com iniciais 'ana'

select distinct first_name
from sales.customers
where first_name like 'ana%';

select distinct first_name 
from sales.customers c 
where first_name Ilike 'ana%';


-- (Exemplo 6) Uso do comando IS NULL
-- Selecionar apenas as linhas que contém nulo no campo "population" na tabela
-- temp_tables.regions

select *
from temp_tables.regions
where population = null;

select *
from temp_tables.regions r 
where population is null;
```

## Funções agregadas

GROUP BY

```sql
-- Serve para agrupar registros semelhantes de uma coluna
-- Normalmente utilizado em conjunto com as Funções de agregação

-- (Exemplo 1) Contagem agrupada de uma coluna
-- Calcule o nº de clientes da tabela customers por estado

select count(*)
from sales.customers

select 
    state, 
    count(customer_id) as "Quantidade"
from sales.customers c
group by state
order by "Quantidade" desc;


-- (Exemplo 2) Contagem agrupada de várias colunas
-- Calcule o nº de clientes por estado e status profissional 

select 
    state, 
    professional_status, 
    count(customer_id) as "Quantidade"
from sales.customers c
group by state, professional_status
order by state, "Quantidade" desc;

-- (Exemplo 3) Seleção de valores distintos
-- Selecione os estados distintos na tabela customers utilizando o group by

select distinct state
from sales.customers

select state 
from sales.customers c 
group by state
order by state;
```

HAVING

```sql
-- Serve para filtrar linhas da seleção por uma coluna agrupada

-- (Exemplo 1) seleção com filtro no HAVING 
-- Calcule o nº de clientes por estado filtrando apenas estados acima de 100 clientes
select 
    state, 
    count(*)
from sales.customers
group by state


select 
    state, 
    count(*)
from sales.customers c
where state <> 'MG'
group by state
having count(*) > 100;
```

## Joins

```sql
-- Servem para combinar colunas de uma ou mais tabelas
-- ALGUM: LEFT, INNER, ALL, etc

select t1.coluna_1, t1.coluna_1, t2.coluna_1, t2.coluna_2
from schema.tabela_1 as t1
ALGUM join schema.tabela_2 as t2
    on condição_de_join;
```

## Union

```sql
select coluna_1, coluna_2
from schema_1.tabela_1

union / union all

select coluna_3, coluna_4 
from schema_2.tabela_2

-- (Exemplo 1) União simples de duas tabelas
-- Una a tabela sales.products com a tabela temp_tables.products_2

select * from sales.products
union all
select * from temp_tables.products_2
```

## Subqueries

```sql
-- Servem para consultar dados de outras consultas.

-- Subquery no WHERE
-- Subquery com WITH
-- Subquery no FROM
-- Subquery no SELECT


-- (Exemplo 1) Subquery no WHERE
-- Informe qual é o veículo mais barato da tabela products

select *
from sales.products p 
where price = (select min(price) from sales.products p2 );


-- (Exemplo 2) Subquery com WITH
-- Calcule a idade média dos clientes por status profissional

with clientes as(
select professional_status, (current_date - birth_date)/365 as idade
from sales.customers c 
)
select professional_status, round(avg(idade),0)
from clientes c
group by professional_status;



-- (Exemplo 3) Subquery no FROM
-- Calcule a média de idades dos clientes por status profissional


select professional_status, round(avg(idade),0)
from (
	select professional_status, (current_date - birth_date)/365 as idade
	from sales.customers c 
) as cliente
group by professional_status;



-- (Exemplo 4) Subquery no SELECT
-- Na tabela sales.funnel crie uma coluna que informe o nº de visitas acumuladas 
-- que a loja visitada recebeu até o momento


select 
f.visit_id,
f.visit_page_date,
s.store_name,
(
select count(*)
from sales.funnel f2 
where f2.visit_page_date  <= f.visit_page_date 
and f2.store_id = f.store_id 

) as vistas_acumuladas
from sales.funnel f 
left join sales.stores s 
on f.store_id = s.store_id
order by s.store_name, f.visit_page_date;
```

## Tratamento de dados

CONVERSÃO DE UNIDADES

```sql
-- Operador ::
-- CAST

-- (Exemplo 1) Conversão de texto em data
-- Corrija a query abaixo utilizando o operador ::

select '2021-10-01' - '2021-02-01'

select '2021-10-01'::date - '2021-02-01'::date



-- (Exemplo 2) Conversão de texto em número
-- Corrija a query abaixo utilizando o operador ::

select '100' - '10'

select '100'::numeric - '10'::numeric


-- (Exemplo 3) Conversão de número em texto
-- Corrija a query abaixo utilizando o operador ::

select replace(112122,'1','A')

select replace(112122::text,'1','A')


-- (Exemplo 4) Conversão de texto em data
-- Corrija a query abaixo utilizando a função CAST

select '2021-10-01' - '2021-02-01'

select cast('2021-10-01' as date) - cast('2021-02-01' as date)
```

TRATAMENTO GERAL

```sql
-- CASE WHEN
-- COALESCE()

-- (Exemplo 1) Agrupamento de dados com CASE WHEN
-- Calcule o nº de clientes que ganham abaixo de 5k, entre 5k e 10k, entre 10k e 
-- 15k e acima de 15k

with faixa_de_renda as (
	select
		income,
		case
			when income < 5000 then '0-5000'
			when income >= 5000 and income < 10000 then '5000-10000'
			when income >= 10000 and income < 15000 then '10000-15000'
			else '15000+'
			end as faixa_renda
	from sales.customers
)

select faixa_renda, count(*)
from faixa_de_renda
group by faixa_renda


-- (Exemplo 2) Tratamento de dados nulos com COALESCE
-- Crie uma coluna chamada populacao_ajustada na tabela temp_tables.regions e
-- preencha com os dados da coluna population, mas caso esse campo estiver nulo, 
-- preencha com a população média (geral) das cidades do Brasil

select * from temp_tables.regions limit 10

-- Opção 1
--select
--	*,
--	case
--		when population is not null then population
--		else (select avg(population) from temp_tables.regions)
--		end as populacao_ajustada
--
--from temp_tables.regions
--
-- Opção 2
--select
--	*,
--	coalesce(population, (select avg(population) from temp_tables.regions)) as populacao_ajustada
--	
--from temp_tables.regions

select 
*
coalesce (population, (select avg(population) from temp_tables.regions)) as populacao_ajustada
from temp_tables.regions;
```

TRATAMENTO DE TEXTO

```sql
-- LOWER()
-- UPPER()
-- TRIM()
-- REPLACE()

-- (Exemplo 1) Corrija o primeiro elemento das queries abaixo utilizando os comandos 
-- de tratamento de texto para que o resultado seja sempre TRUE 

select upper('São Paulo') = 'SÃO PAULO'


select lower('São Paulo') = 'são paulo'


select trim('SÃO PAULO     ') = 'SÃO PAULO'


select replace('SAO PAULO', 'SAO', 'SÃO') = 'SÃO PAULO'
```

TRATAMENTO DE DATAS

```sql
-- INTERVAL
-- DATE_TRUNC
-- EXTRACT
-- DATEDIFF

-- (Exemplo 1) Soma de datas utilizando INTERVAL
-- Calcule a data de hoje mais 10 unidades (dias, semanas, meses, horas)

select current_date + 10
select (current_date + interval '10 weeks')::date 
select (current_date + interval '10 months')::date
select current_date + interval '10 hours'


-- (Exemplo 2) Truncagem de datas utilizando DATE_TRUNC
-- Calcule quantas visitas ocorreram por mês no site da empresa

select date_trunc('month', visit_page_date)::date as meses,
count(*)
from sales.funnel
group by visit_page_date
order by visit_page_date desc



-- (Exemplo 3) Extração de unidades de uma data utilizando EXTRACT
-- Calcule qual é o dia da semana que mais recebe visitas ao site

select
	'2022-01-30'::date;

	
select 
extract('dow' from visit_page_date::date) as dia_da_semana,
count(*)
from sales.funnel
group  by dia_da_semana
order by dia_da_semana;


-- (Exemplo 4) Diferença entre datas com operador de subtração (-) 
-- Calcule a diferença entre hoje e '2018-06-01', em dias, semanas, meses e anos.

select (current_date - '2018-06-01'::date) as dias
select (current_date - '2018-06-01'::date)/7 as semanas
select (current_date - '2018-06-01'::date)/30 as meses
select (current_date - '2018-06-01'::date)/365 as anos
```

FUNÇÕES

```sql
-- Servem para criar comandos personalizados de scripts usados recorrentemente.

-- (Exemplo 1) Crie uma função chamada DATEDIFF para calcular a diferença entre
-- duas datas em dias, semanas, meses, anos

select (current_date - '2018-06-01')
select (current_date - '2018-06-01')/7
select (current_date - '2018-06-01')/30
select (current_date - '2018-06-01')/365

select datediff('y', '2023-03-07', current_date)

create function datediff(unidade varchar, data_inicial date, data_final date)
returns integer
language sql

as

$$
	select 
	case 
		when unidade in ('d', 'day', 'days') then (data_final - data_inicial)
		when unidade in ('w', 'week', 'weeks') then (data_final - data_inicial)/7
		when unidade in ('m', 'month', 'months') then (data_final - data_inicial)/30
		when unidade in ('y', 'year', 'years') then (data_final - data_inicial)/365
	end as diferenca
	
$$



-- (Exemplo 2) Delete a função DATEDIFF criada no exercício anterior

drop function datediff
```

## Manipulação de tabelas

CRIAÇÃO E DELEÇÃO

```sql
-- Criação de tabela a partir de uma query
-- Criação de tabela a partir do zero
-- Deleção de tabelas

-- (Exemplo 1) Criação de tabela a partir de uma query
-- Crie uma tabela chamada customers_age com o id e a idade dos clientes. 
-- Chame-a de temp_tables.customers_age

select customer_id,
datediff('years', birth_date, current_date)
into temp_tables.customers_age
from sales.customers

select * from temp_tables.customers_age;

-- (Exemplo 2) Criação de tabela a partir do zero
-- Crie uma tabela com a tradução dos status profissionais dos clientes. 
-- Chame-a de temp_tables.profissoes


select distinct professional_status 
from sales.customers

create table temp_tables.profissoes(
professional_status varchar,
status_profissional varchar
);


insert into temp_tables.profissoes(professional_status, status_profissional)
values
('freelancer','freelancer'),
('retired','aposentado(a)'),
('clt','clt'),
('self_employed','autônomo(a)'),
('other','outro'),
('businessman','empresário(a)'),
('civil_servant','funcionário público '),
('student','estudante')


select * from temp_tables.profissoes;

-- (Exemplo 3) Deleção de tabelas
-- Delete a tabela temp_tables.profissoes


drop table temp_tables.profissoes;
```

LINHAS - INSERÇÃO, ATUALIZAÇÃO E DELEÇÃO

```sql
-- Inserção de linhas
-- Atualização de linhas
-- Deleção de linhas

-- (Exemplo 1) Inserção de linhas
-- Insira os status 'desempregado(a)' e 'estagiário(a)' na temp_table.profissoes

create table temp_tables.profissoes (
	professional_status varchar,
	status_profissional varchar
);

insert into temp_tables.profissoes
(professional_status, status_profissional)
values
('freelancer', 'freelancer'),
('retired', 'aposentado(a)'),
('clt', 'clt'),
('self_employed', 'autônomo(a)'),
('other', 'outro'),
('businessman', 'empresário(a)'),
('civil_servant', 'funcionário público(a)'),
('student', 'estudante')


insert into temp_tables.profissoes(professional_status, status_profissional)
values
('unemployed', 'desempregado(a)'),
('trainee', 'estagiário')


-- (Exemplo 2) Atualização de linhas
-- Corrija a tradução de 'estagiário(a)' de 'trainee' para 'intern' 

update temp_tables.profissoes
set professional_status = 'intern'
where status_profissional = 'estagiário(a)'

-- (Exemplo 3) Deleção de linhas
-- Delete as linhas dos status 'desempregado(a)' e 'estagiário(a)'

delete from temp_tables.profissoes
where status_profissional = 'desempregado(a)' or status_profissional = 'estagiário'
```

COLUNAS - INSERÇÃO, ATUALIZAÇÃO E DELEÇÃO

```sql
-- Inserção de colunas
-- Alteração de colunas
-- Deleção de colunas

-- (Exemplo 1) Inserção de Colunas
-- Insira uma coluna na tabela sales.customers com a idade do cliente

alter table sales.customers
add customer_age int

-- (Exemplo 2) Alteração do tipo da coluna
-- Altere o tipo da coluna customer_age de inteiro para varchar

alter table sales.customers
alter column customer_age type varchar

-- (Exemplo 3) Alteração do nome da coluna
-- Renomeie o nome da coluna "customer_age" para "age"

alter table sales.customers
rename column customer_age to age

-- (Exemplo 4) Deleção de coluna
-- Delete a coluna "age"

alter table sales.customers
drop column age
```