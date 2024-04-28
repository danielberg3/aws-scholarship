SELECT     
    count(disciplina),
    sum(CAST(vagas AS integer))
from s3object
where lower(disciplina) = 'matemática' and modalidade = 'Integrado'