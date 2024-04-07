import pandas as pd

alunos_dict = {
    'Nome': ['Lorenzo', 'Lucca', 'Arthur', 'Leonardo'],
    'Nota': [4, 6, 5.5, 9],
    'Aprovado': []
}

alunos_dict['Aprovado'] = list(map(lambda nota: '\033[1;32mSim\033[m' if nota >= 6 else '\033[1;31mNão\033[m', alunos_dict['Nota']))

alunos_dataframe = pd.DataFrame(alunos_dict)
print(alunos_dataframe)

print()

# Filtrando Colunas
print(alunos_dataframe['Nome'])

print()

# Filtrando linhas
print(alunos_dataframe.loc[[0]])
print()
print(alunos_dataframe.loc[[0,3,2]])
print()
print(alunos_dataframe.loc[0:2])

print()

print(alunos_dataframe.loc[alunos_dataframe['Aprovado'] == '\033[1;32mSim\033[m'])
