# Exercícios de consulta SQL

**E01**

Apresente a query para listar todos os livros publicados após 2014. Ordenar pela coluna cod, em ordem crescente, as linhas.  Atenção às colunas esperadas no resultado final: cod, titulo, autor, editora, valor, publicacao, edicao, idioma

``` bash
    select *
    from livro
    where publicacao > '2014-12-31'
    order by cod;
```

**E02**

Apresente a query para listar os 10 livros mais caros. Ordenar as linhas pela coluna valor, em ordem decrescente.  Atenção às colunas esperadas no resultado final:  titulo, valor.

``` bash
   select 
        titulo,
        valor
   from livro 
   order by valor desc
   limit 10; 
```

**E03**

 Apresente a query para listar as 5 editoras com mais livros na biblioteca. O resultado deve conter apenas as colunas quantidade, nome, estado e cidade. Ordenar as linhas pela coluna que representa a quantidade de livros em ordem decrescente.

``` bash
    select
    count(l.titulo) as quantidade,
        e.nome,
        a.estado,
        a.cidade
    from editora e
    left join livro l
        on e.codEditora = l.editora
    left join endereco a
        on e.endereco = a.codEndereco
    group by e.nome, a.estado, a.cidade
    having quantidade > 0 
    order by quantidade desc
    limit 5;
```

**E04**

Apresente a query para listar a quantidade de livros publicada por cada autor. Ordenar as linhas pela coluna nome (autor), em ordem crescente. Além desta, apresentar as colunas codautor, nascimento e quantidade (total de livros de sua autoria).

``` bash
   select
        a.nome,
        a.codAutor,
        a.nascimento,
    count(l.autor) as quantidade
    from autor a
    left join livro l
        on a.codAutor = l.autor
    group by a.nome
    order by a.nome;     
```

**E05**

Apresente a query para listar o nome dos autores que publicaram livros através de editoras NÃO situadas na região sul do Brasil. Ordene o resultado pela coluna nome, em ordem crescente. Não podem haver nomes repetidos em seu retorno.

``` bash
    select distinct a.nome
    from autor a
    inner join livro l
        on a.codAutor = l.autor
    inner join editora edit
        on l.editora = edit.codEditora
    inner join endereco e
        on edit.endereco = e.codEndereco
    where e.estado not in ('PARANÁ', 'SANTA CATARINA', 'RIO GRANDE DO SUL')
    order by a.nome;
```

**E06**

Apresente a query para listar o autor com maior número de livros publicados. O resultado deve conter apenas as colunas codautor, nome, quantidade_publicacoes.

``` bash
    select 
        a.codAutor,
        a.nome,
        count(*) as quantidade_publicacoes
    from autor a
    inner join livro l
        on a.codAutor = l.autor
    group by a.nome
    order by quantidade_publicacoes desc
    limit 1;
```

**E07**

Apresente a query para listar o nome dos autores com nenhuma publicação. Apresentá-los em ordem crescente.

``` bash
    with quantidade as(
        select distinct
            a.nome,
            count(l.titulo) as quantidade_livros
        from autor a
        left join livro l
            on a.codAutor = l.autor
        group by a.nome

    )
    select distinct
        a.nome
    from autor a
    left join quantidade q
        on a.nome = q.nome
    where q.quantidade_livros = 0
    order by a.nome;
```

**E08**

Apresente a query para listar o código e o nome do vendedor com maior número de vendas (contagem), e que estas vendas estejam com o status concluída.  As colunas presentes no resultado devem ser, portanto, cdvdd e nmvdd.

``` bash
    with maior as (
        select
            vendedor.cdvdd,
            vendedor.nmvdd,
            count(vendas.cdvdd) as quantidade
        from tbvendedor vendedor
        left join tbvendas vendas
            on vendedor.cdvdd = vendas.cdvdd 
        group by vendedor.cdvdd, vendedor.nmvdd
        order by quantidade desc 
    )
    select 
        m.cdvdd,
        m.nmvdd
    from maior m
    limit 1;
```

**E09**

Apresente a query para listar o código e nome do produto mais vendido entre as datas de 2014-02-03 até 2018-02-02, e que estas vendas estejam com o status concluída. As colunas presentes no resultado devem ser cdpro e nmpro.

``` bash
    with produtos as (
        select 
            pro.cdpro codigo,
            ven.nmpro nome,
            count(ven.cdpro) as quantidade
        from tbestoqueproduto pro
        left join tbvendas ven
            on pro.cdpro = ven.cdpro
        where ven.dtven between '2014-02-03' and '2018-02-02' and ven.status = 'Concluído'
        group by pro.cdpro
        order by quantidade desc
    )

    select 
        produtos.codigo cdpro,
        produtos.nome nmpro
    from produtos
    limit 1;
```

**E10**

A comissão de um vendedor é definida a partir de um percentual sobre o total de vendas (quantidade * valor unitário) por ele realizado. O percentual de comissão de cada vendedor está armazenado na coluna perccomissao, tabela tbvendedor. 

Com base em tais informações, calcule a comissão de todos os vendedores, considerando todas as vendas armazenadas na base de dados com status concluído.

As colunas presentes no resultado devem ser vendedor, valor_total_vendas e comissao. O valor de comissão deve ser apresentado em ordem decrescente arredondado na segunda casa decimal.

``` bash
    select 
        vendedor.nmvdd as vendedor,
        sum(vendas.qtd * vendas.vrunt) as valor_total_vendas,
        round((sum(vendas.qtd * vendas.vrunt) * vendedor.perccomissao/100), 2) as comissao
    from tbvendedor vendedor
    left join tbvendas vendas
        on vendedor.cdvdd = vendas.cdvdd
    where vendas.status = 'Concluído'
    group by vendedor.nmvdd
    order by comissao desc;
```

**E11**

Apresente a query para listar o código e nome cliente com maior gasto na loja. As colunas presentes no resultado devem ser cdcli, nmcli e gasto, esta última representando o somatório das vendas (concluídas) atribuídas ao cliente.

``` bash
    select 
        cdcli,
        nmcli,
        sum(vrunt * qtd) as gasto
    from tbvendas
    where status = 'Concluído'
    group by cdcli
    order by gasto desc
    limit 1;
```

**E12**

Apresente a query para listar código, nome e data de nascimento dos dependentes do vendedor com menor valor total bruto em vendas (não sendo zero). As colunas presentes no resultado devem ser cddep, nmdep, dtnasc e valor_total_vendas.


Observação: Apenas vendas com status concluído.

``` bash
    with menor as(
        select 
            vendedor.cdvdd as codigo,
            vendedor.nmvdd as vendedor,
            sum(vendas.qtd * vendas.vrunt) as valor_total_vendas
        from tbvendedor vendedor
        inner join tbvendas vendas
            on vendedor.cdvdd = vendas.cdvdd
        where vendas.status = 'Concluído'
        group by vendedor
        order by valor_total_vendas
        limit 1
    )

    select
        dependente.cddep,
        dependente.nmdep,
        dependente.dtnasc,
        menor.valor_total_vendas
    from menor
    left join tbdependente as dependente
        on  menor.codigo = dependente.cdvdd;   
```

**E13**

Apresente a query para listar os 10 produtos menos vendidos pelos canais de E-Commerce ou Matriz (Considerar apenas vendas concluídas).  As colunas presentes no resultado devem ser cdpro, nmcanalvendas, nmpro e quantidade_vendas.

``` bash
    select
        pro.cdpro,
        ven.nmcanalvendas,
        ven.nmpro,
        sum(qtd) quantidade_vendas
    from tbestoqueproduto pro
    left join tbvendas ven
        on pro.cdpro = ven.cdpro
    where ven.nmcanalvendas in ('Ecommerce', 'Matriz') and ven.status = 'Concluído'
    group by ven.nmcanalvendas, pro.cdpro
    order by quantidade_vendas
    limit 10; 
```

**E14**

Apresente a query para listar o gasto médio por estado da federação. As colunas presentes no resultado devem ser estado e gastomedio. Considere apresentar a coluna gastomedio arredondada na segunda casa decimal e ordenado de forma decrescente.

Observação: Apenas vendas com status concluído.

``` bash
    select 
        estado,
        round((sum(qtd * vrunt)/cast(count(cdcli) as float)), 2) as gastomedio
    from tbvendas
    where status = 'Concluído'
    group by estado
    order by gastomedio desc;
```

**E15**

Apresente a query para listar os códigos das vendas identificadas como deletadas. Apresente o resultado em ordem crescente.

``` bash
    select
        cdven
    from tbvendas
    where deletado = '1';
```

**E16**

Apresente a query para listar a quantidade média vendida de cada produto agrupado por estado da federação. As colunas presentes no resultado devem ser estado e nmprod e quantidade_media. Considere arredondar o valor da coluna quantidade_media na quarta casa decimal. Ordene os resultados pelo estado (1º) e nome do produto (2º).

Obs: Somente vendas concluídas.

``` bash
    select 
        estado,
        nmpro,
        round(sum(qtd) / cast(count(cdcli) as float), 4) quantidade_media
    from tbvendas
    where status = 'Concluído'
    group by estado, nmpro
    order by estado, nmpro;
```