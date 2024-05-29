import pandas as pd

dados = pd.read_csv("C:/Users/l50038499/Desktop/athlete_events.csv")
print(dados.head())
print(dados.keys())

dados.rename(columns={'Name': 'Lorenzo'}, inplace=True)  # O inplace mostra o resultado
print(dados.head())

print('-' * 50)

lorenzo = dados['Lorenzo']
print(lorenzo)
print(type(lorenzo))

print('-' * 50)

print(dados['Age'].value_counts())  # Conta a qnt de dados q cd idade tem

print('-' * 50)

print(dados.describe())  # faz varios tipos de contas nas colunas que tem números
