class Actor:
    def __init__(self, Actor, Total_Gross, Number_of_Movies, Average_per_Movie, Movie_best, Gross):
        self.Actor = Actor
        self.Total_Gross = Total_Gross
        self.Number_of_Movies = Number_of_Movies
        self.Average_per_Movie = Average_per_Movie
        self.Movie_best = Movie_best
        self.Gross = Gross


lista_atores = []

def percorrer_csv(arquivo):
    with open(arquivo, 'r') as atores:
        cabecalho = "Actor,Total Gross,Number of Movies,Average per Movie,#1 Movie,Gross\n"
        
        for ator in atores:
            if str(ator) != cabecalho:
                ator = ator.replace('"','').strip('\n').split(',')
                if len(ator) == 6:
                    objeto_ator = Actor(ator[0], float(ator[1]), int(ator[2]), float(ator[3]), ator[4], float(ator[5]))
                    lista_atores.append(objeto_ator)
                else:
                    objeto_ator = Actor(ator[0] + ator[1], float(ator[2]), int(ator[3]), float(ator[4]), ator[5], float(ator[6]))
                    lista_atores.append(objeto_ator)

def possui_mais_filmes(arquivo):
    mais_filmes = 0
    nome_ator = ''
    for ator in lista_atores:
        if ator.Number_of_Movies > mais_filmes:
            mais_filmes = ator.Number_of_Movies
            nome_ator = ator.Actor
    
    with open(arquivo, 'w') as saida:
        print(f'{nome_ator}, {mais_filmes}', file=saida)


def media_principais_filmes(arquivo):
    filmes = {}
    for ator in lista_atores:
        filmes[ator.Movie_best] = ator.Gross
    

    valor_filmes = sum(filmes.values())    
    media_filmes = valor_filmes / len(filmes)
    with open(arquivo, 'w') as saida:
        print(f'{round(media_filmes, 2)}', file=saida)


def maior_media_bilheteria(arquivo):
    maior_media_bilheteria = 0
    nome_ator = ''
    for ator in lista_atores:
        if ator.Average_per_Movie > maior_media_bilheteria:
            maior_media_bilheteria = ator.Average_per_Movie
            nome_ator = ator.Actor
    
    with open(arquivo, 'w') as saida:
        print(f'{nome_ator}', file=saida)


def filmes_mais_vistos(arquivo):
    mais_vistos = [ator.Movie_best for ator in lista_atores]
    filmes = {}

    for ator in lista_atores:
        quantidade = mais_vistos.count(ator.Movie_best)
        filmes[ator.Movie_best] = quantidade 
    
    
    filmes = sorted(filmes.items(), key=lambda x: x[0])
    filmes = sorted(filmes, key=lambda x: x[1], reverse=True)

    with open(arquivo, 'w') as saida:
        for indice, filme in enumerate(filmes):
            print(f'{indice} - O filme {filme[0]} aparece {filme[1]} vez(es) no dataset', file=saida)
       

def atores_maior_bilheteria(arquivo):
    atores =[]

    for ator in lista_atores:
        atores.append(tuple([ator.Actor, ator.Total_Gross]))
    
    atores = sorted(atores, key=lambda x: x[1], reverse=True)
    with open(arquivo, 'w') as saida:
        for ator in atores:
            print(f'{ator[0]} - {ator[1]}', file=saida)


percorrer_csv('actors.csv')
possui_mais_filmes('etapa-1.txt')
media_principais_filmes('etapa-2.txt')
maior_media_bilheteria('etapa-3.txt')
filmes_mais_vistos('etapa-4.txt')
atores_maior_bilheteria('etapa-5.txt')
