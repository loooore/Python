import pandas as pd

dados = pd.read_excel("C:/Users/l50038499/Desktop/pandas 1.xlsx")

print(dados.head())

a = dados.drop('DU ID', axis=1, inplace=True)   # axis = 0 - Linha / axis = 1 - coluna
# Drop remove a coluna

print(a)