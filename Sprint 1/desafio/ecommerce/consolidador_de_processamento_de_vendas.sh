# entrar na pasta onde estão os relatórios

cd /home/daniel/Documentos/aws-scholarship/Sprint\ 1/desafio/ecommerce/vendas/backup

# Variável com o nome do arquivo relatorio_final.txt

relatorio_final="relatorio_final.txt"

# loop pelo arquivos .txt exceto relatorio_final.txt

for file in *.txt; do
   
    if [ "$file" != "$relatorio_final" ]; then
        cat "$file" >> "$relatorio_final"
    fi
done

# movendo relatorio_final.txt para pasta eccomerce

mv "$relatorio_final" /home/daniel/Documentos/aws-scholarship/Sprint\ 1/desafio/ecommerce
