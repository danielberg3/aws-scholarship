# Spark

O Spark é um ferramenta de processamendo de dados que permite que os dados sejam armazenados e separados em clusters, garantido acesso mais rápido, além de segurança contra perdas de dados devido as cópias de dados que são feitas pelos nós.

## Comandos essencias do spark

Criar schema:

```python
clienteSchema = "Id INT, Cliente STRING, Estado STRING, Sexo STRING, Status STRING"
```

importar dados com spark:

```python
cliente = spark.read.format("parquet").load("/home/daniel/download/Atividades/Clientes.parquet", schema=clienteSchema)
```

Consulta no DataFrame com filtragem de dados:

```python
cliente.select("Cliente", 'Estado', 'Status').where((Func.col('Status') == 'Gold') | (Func.col('Status') == 'Platinum')).show()
```

Fazer inner join nos DataFrames em conjunto com  a função de agregação count()

```python
cliente.join(venda, cliente.ClienteID == venda.ClienteID, 'inner').select(cliente.Status).groupBy(cliente.Status).count().show(truncate=False)
```

Comando para salvar dados de um DataFrame no disco:

```python
cliente.write.format("parquet").save("/home/daniel/dfimportparquet")
```

### Spark SQL

Criar banco de dados com spark e utilizar o mesmo

```python
spark.sql("create database sao")
spark.sql("use sao").show()
```

Criar tabela no banco a partir de um DataFrame

```python
cliente.write.saveAsTable("Clientes")
```

Fazer select na tabela criada

```python
spark.sql("select * from clientes").show
```

alterar registros de uma tabela (overwrite/append)

```python
despachantes.write.mode("overwrite").saveAsTable("Clientes")
```

Criar tabela não gerenciada

```python
despachantes.write.option("path", "/home/daniel/clienteparquet").saveAsTable("cliente_ng")
```

Ver se as tabelas são gerenciadas ou não

```python
spark.catalog.listTables()
```

Criar view temporária

```python
	spark.sql("CREATE OR REPLACE TEMP VIEW DESP_VIEW AS select * from despachantes")
```

Criar view global

```python
	spark.sql("CREATE OR REPLACE GLOBAL TEMP VIEW DESP_VIEW2 AS select * from despachantes")
```

Fazer join utilizando SQL no spark

```python
spark.sql("select reclamacoes.*, despachantes.nome from despachantes inner join reclamacoes on (despachantes.id = reclamacoes.iddesp)").show()
```

Fazer join utilizando dataFrame:

```python
despachantes.join(reclamacoes, despachantes.id = reclamacoes.iddesp, "inner").select("idrec", "iddesp", "nome").show()
```

Comando para entrar no shell onde é possível executar sql puro:

```python
spark-sql
```

### Criando aplicações

```python
import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

if __name__ == "__main__":
	spark = SparkSession.builder.appName("Exemplo").getOrCreate()
	arqschema = "id INT, nome STRING, status STRING, cidade STRING, vendas INT, data STRING"
	despachantes = spark.read.csv(sys.argv[1], header=False, schema = arqschema)
	calculo = despachantes.select("data").groupBy(year("data")).count()
	calculo.write.format("console").save()
	spark.stop()
	
	
	# Executar no console: spark-submit aplicativo.py /home/daniel/download/despachantes.csv
```

### Otimização

Definir partições de uma tabela com base em uma coluna específica:

```python
churn.write.partitionBy("Geography").saveAsTable("churn_Geo")
```

Criar buckets a partir de uma coluna:

```python
churn.write.bucketBy(3,"Geography").saveAsTable("churn_Geo2")
```