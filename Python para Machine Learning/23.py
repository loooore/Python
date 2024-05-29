import pandas as pd
import numpy as np
import seaborn as sns

data = pd.read_csv("C:/Users/l50038499/Desktop/athlete_events.csv")

# Imprime os 5 primeiras linhas
print(data.head())

print()
print('-'*50)
print()

# Imprime as 5 últimas linhas
print(data.tail())

print()
print('-'*50)
print()

# Imprime a qnt de linhas e colunas
print(f'linhas: {data.shape[0]} \n colunas: {data.shape[1]}')

print()
print('-'*50)
print()

# Imprime a dados gerais sobre o dataset
print(data.describe())

print()
print('-'*50)
print()

# Retornam o nome das colunas
print(data.columns)
# print(data.keys())

print()
print('-'*50)
print()

# Imprime os valores únicos
print(data.nunique())
print()
print(data['Medal'].unique())

print()
print('-'*50)
print()


# LIMPADO O DATASET


# Imprimindo os valores nulos
print(data.isnull())
print()
print(data.isnull().sum())

print()



print()
print('-'*50)
print()

# Removendo ID
idRemoved = data.drop(['ID'], axis=1)
print(idRemoved.head())

print()
print('-'*50)
print()


