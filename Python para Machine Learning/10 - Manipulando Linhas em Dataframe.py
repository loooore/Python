import pandas as pd

alunos_dict = {
    'Nome': ['Lorenzo', 'Lucca', 'Arthur', 'Leonardo'],
    'Nota': [4, 6, 5.5, 9],
    'Aprovado': []
}

alunos_dict['Aprovado'] = list(map(lambda nota: 'Sim' if nota >= 6 else 'Não', alunos_dict['Nota']))

alunos_dataframe = pd.DataFrame(alunos_dict)
print(alunos_dataframe)

print()

primeiras_linhas = alunos_dataframe.loc[0:2]
print(primeiras_linhas)

print()

novo_dataframe = alunos_dataframe.loc[alunos_dataframe['Nota'] != 9]
print(novo_dataframe)

