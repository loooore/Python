import pandas as pd

dados = pd.read_excel('C:/Users/l50038499/Desktop/pandas 1.xlsx')

print(dados.head(10))  # Lendo os arquivos

print()

dados2 = pd.read_csv('C:/Users/l50038499/Desktop/athlete_events.csv')
print(dados2.head())