#voce foi contratado para analisar uma planilha de musicas chamadas ClassicDiscocsv,
#contendo informações sobre músicas clássicas de discoteca, com as seguintes colunas
#Artista
#Musica
#Ano
#Genero
#Seu objetivo é explorar os dados usando diferentes metodos da biblioteca pandas.

import pandas as pd

df = pd.read_csv('ClassicDisco.csv')

filtro = df['Artist']
print(filtro)

#import pandas as pd

df = pd.read_csv('ClassicDisco.csv')

filtro = df['Track']
print(filtro)

#import pandas as pd

df = pd.read_csv('ClassicDisco.csv')

filtro = df['Year']
print(filtro)

#import pandas as pd

df = pd.read_csv('ClassicDisco.csv')

filtro = df['Album']
print(filtro)