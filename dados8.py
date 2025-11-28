import pandas as pd

df = pd.read_csv('ClassicDisco.csv')

#Filtrar musicas Lançadas depois de 1980. Mostre apenas as colunas 'Year' e 'Track'
print(df[df['Year'] < 1980] [['Year', 'Track']])

