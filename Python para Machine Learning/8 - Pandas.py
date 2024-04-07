import pandas as pd

alunos_dict = {
    'Nome': ['Lorenzo', 'Lucca', 'Arthur', 'Leonardo'],
    'Nota': [4, 6, 5.5, 9],
    'Aprovado': []
}
alunos_dict['Aprovado'] = ['\033[1;32mSim\033[m' if nota >= 6 else '\033[1;31mNão\033[m' for nota in alunos_dict['Nota']]

alunos_dataframe = pd.DataFrame(alunos_dict)
print(alunos_dataframe)

print(alunos_dataframe.shape)

print(alunos_dataframe.describe())

print()

