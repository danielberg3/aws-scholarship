SELECT 
    disciplina,
    curso,
    campus,
    UPPER(modalidade),
    CASE
        WHEN CAST(ch AS integer) <= 60 THEN 'Baixa carga horária'
        WHEN CAST(ch AS integer) > 60 AND CAST(ch AS integer) <= 80 THEN 'Média carga horária'
        WHEN CAST(ch AS integer) > 80 THEN 'Alta carga horária'
    END AS "Carga horária",
    (EXTRACT(YEAR FROM UTCNOW()) - CAST(SUBSTRING(periodo, 1, 4) AS integer)) * CAST(vagas AS integer)
FROM s3object
WHERE (campus = 'CAMPUS MACEIO' OR campus = 'CAMPUS ARAPIRACA') AND modalidade = 'Integrado' 
limit 10