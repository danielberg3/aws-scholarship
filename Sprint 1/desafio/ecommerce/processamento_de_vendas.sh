# entrar na pasta ecommerce

cd /home/daniel/Documentos/aws-scholarship/Sprint\ 1/desafio/ecommerce

# criar diretório vendas

mkdir -p vendas

# copiar arquivo dados_de_vendas.csv

cp dados_de_vendas.csv ./vendas
cd ./vendas

# limpeza e ordenação do arquivo dados_de_vendas.csv

awk -F ',' 'NF == 5 {print > "auxiliar.csv"; next}' dados_de_vendas.csv && mv auxiliar.csv dados_de_vendas.csv

awk 'BEGIN {count=0} /^id,produto,quantidade,preço,data$/ {if (count==1) next; count++} {print}' dados_de_vendas.csv > auxiliar.csv && mv auxiliar.csv dados_de_vendas.csv

awk -F ',' 'NR > 1 {split($NF, date_parts, "/"); print date_parts[3] "/" date_parts[2] "/" date_parts[1] "," $0}' dados_de_vendas.csv | sort -t ',' -k1,1 | cut -d ',' -f 2- > auxiliar.csv
mv auxiliar.csv dados_de_vendas.csv

echo "id,produto,quantidade,preço,data" > auxiliar.csv
cat dados_de_vendas.csv >> auxiliar.csv
mv auxiliar.csv dados_de_vendas.csv

 

# criar subdiretório backup

mkdir -p backup

# copiar arquivo dados_de_vendas.csv  para dentro do diretório backup

data_atual=$(date +"%Y%m%d")
nome_arquivo="dados-${data_atual}.csv"
cp dados_de_vendas.csv ./backup/"$nome_arquivo"
cd ./backup

# renomear arquivo csv

mv "$nome_arquivo" "backup-$nome_arquivo"

# criar arquivo relatorio.txt

relatorio="relatorio-${data_atual}.txt"
touch "$relatorio"

# colocar data atual dentro do arquivo relatório.txt

data=$(date +"%Y/%m/%d %H:%M")
echo "$data" > "$relatorio"

# colocar a data da primeira venda dentro do arquivo relatório.txt

primeira_venda=$(awk -F ',' 'NR==2 {print $5}' "backup-$nome_arquivo")
echo "Primeira venda: $primeira_venda" >> "$relatorio"

# colocar a data da última venda dentro do arquivo relatório.txt

ultima_venda=$(awk -F ',' 'END {print $5}' "backup-$nome_arquivo")
echo "Última venda: $ultima_venda" >> "$relatorio"

# quantidade de itens diferentes vendidos

itens_vendidos=$(awk -F ',' 'NR > 1 { itens_vendidos[$2]++ } END { print length(itens_vendidos) }' "backup-$nome_arquivo")
echo "Quantidade dos diferentes itens vendidos: $itens_vendidos" >> "$relatorio"

# adicionar cabeçalho mais as 10 primeiras do arquivo.csv no relatório.txt

echo "" >> "$relatorio"
linhas_arquivo=$(head -n 11 "backup-$nome_arquivo")
echo "$linhas_arquivo"
echo "$linhas_arquivo" >> "$relatorio"
echo "" >> "$relatorio"

# compactar arquivo de backup como zip

arquivo_sem_extensao=$(basename "backup-$nome_arquivo" .csv)
zip -r -m "$arquivo_sem_extensao".zip "backup-$nome_arquivo"

# Apagar arquivo dados_de_vendas.csv do diretório vendas

cd ..
rm dados_de_vendas.csv


















