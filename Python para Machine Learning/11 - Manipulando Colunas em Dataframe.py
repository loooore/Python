import pandas as pd


dados = pd.read_excel("C:/Users/l50038499/Desktop/pandas 1.xlsx")
print(dados.head())
print(dados.keys())

dados.rename(columns={'DU ID': 'Lorenzo'}, inplace=True) # O inplace mostra o resultado
print(dados.head())

print('-'*50)

lorenzo = dados['Lorenzo']
print(lorenzo)
print(type(lorenzo))

print('-'*50)

print(dados['Project Name'].value_counts())

print('-'*50)

print(dados.describe()) # faz varios tipos de contas nas colunas que tem números