import pandas as pd

df = pd.read_csv('ClassicDisco.csv')

#Filtrar musicas Lançadas depois de 1980
print(df[df['Year'] > 1980])
