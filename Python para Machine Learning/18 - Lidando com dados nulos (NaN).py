import pandas as pd

dados = pd.read_csv("C:/Users/l50038499/Desktop/athlete_events.csv")
print(dados.shape)

dados2 = dados.dropna()  # Exclui as linhas que tenha NaN
print(dados2.shape)

print('-' * 50)

enulo = dados.isnull()  # False - não nulo | True - Nulo
print(enulo.head(100))

print('-' * 50)

faltantes = dados.isnull().sum()
print(faltantes)

print('-' * 50)

# Dividindo a qnt de dados nulos, pela qnt de dados totais ( só dividir pelo comprimento de uma das colunas
faltantes_pecentual = (dados.isnull().sum() / len(dados['ID']))
print(faltantes_pecentual * 100)

print('-' * 50)

dados.fillna({'Medal': 'None'}, inplace=True)  # Vai substituir os dados nulos da coluna Medal
dados.fillna({'Age': dados['Age'].mean()}, inplace=True)  # Vai substituir os nulos da coluna Age pela média das idades
dados.fillna({'Height': dados['Height'].mean()}, inplace=True)
dados.fillna({'Weight': dados['Weight'].mean()}, inplace=True)

print(dados.head(100))

dados_nulos = (dados.isnull().sum() / len(dados['ID']))
print(dados_nulos)
