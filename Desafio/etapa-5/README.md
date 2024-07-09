# Desafio

Nesta Etapa do desafio foi realizado comsumo de dados do data lake para gerar informação através do dashboard criado na ferramenta quicksight. Cada criada deu origem a um gráfico, portanto irei explicar como respondi cada uma das perguntas.

## Perguntas

As perguntas feitas a seguir são aplicadas a um período de anos conforme for definido no controle de data criado na análise do quicksight, trata-se de um filtro deslizante onde é colocado o período de anos em que a análise deve ser feita.

**1. Qual a média geral de avaliação dos filmes da base de dados?**

Para respoder essa pergunta foi criada uma KPI que possuía a média dos valores da coluna notaMedia.

**2. Qual a maior nota obtida para os filmes?**

Aqui foi criada uma KPI que possuía a maior entre os valores da coluna notaMedia.

**3. Qual a quantidade de atuações média dos atores?**

Para este caso foi criado um campo calculado que tinha quantidade de participações do ator nas obras, em seguida foi criada uma KPI que possuía a média dos valores dessa coluna.

**4. Quantos filmes foram produzidos para os gêneros drama, romance e drama/romance?**

Nesta pergunta foi criado um gráfico de donut, nele foi feito um agrupamento dos filmes pela coluna genero, a qual tinha como valor as três possiblidades estabelecidas na pergunta, a coluna usada para estabelecer a quantidade de vezes que cada gênero aparecia foi a idObra, sobre a qual foi feita uma contagem de id's distinta.

**5. Qual a média das avaliações para os gêneros drama, romance e drama/romance?**

Neste momento foi criado um gráfico de barras com gêneros de filmes (drama, romance e drama/romance) no eixo X, foi calculada a média da coluna notaMedia por gênero no eixo Y.

**6. Quais os 5 filmes mais votados dos gêneros drama e romance?**

Nessa resposta foi criado um gráfico de barras verticais, nele os títulos dos filmes era apresentado no eixo Y e a nota média do filme era apresentado no eixo X, para selecionar os filmes foi criado um filtro no gráfico para que apresentasse apenas o 5 primeiros filmes com mais votos.

**7. Para cada um dos filmes obtidos na análise anterior de forma individual, quais foram os atores que participaram e quantas outras atuações tiveram dentro do gênero de drama e romance?**

Essa etapa foi um tanto peculiar, pois para apresentar os atores de filmes um filme por vez eu precisava de um controle de lista contendo exclusivamente os 5 filmes mais votados. Contudo, para que isso funcionasse eu precisaria que fosse aplicado um filtro sobre o controle e o controle já é aplicado sobre um filtro. Como não encontrei uma forma de fazer isso optei por uma outra solução.

Minha solução foi criar um gráfico com o número de participações do ator no eixo Y e o nome do ator no eixo X. Logo em seguida criei uma tabela com a coluna de título do filme ordenada pelo numero de votos, porém escondi a coluna de número de votos. Assim, transformei a tabela em uma ação, de modo que os dados de atores de uma filme eram exibidos conforme eu clicava em um dos filmes da tabela.

# Dashboard

![dashboard de filmes](evidencias/Desempenho%20dos%20filmes%20de%20drama%20e%20romance%20ao%20longo%20dos%20anos_page-0001.jpg)