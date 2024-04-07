import numpy as np
import pandas as pd

alunos = {
    'Nome': ['Lorenzo', 'Lucca', 'Arthur', 'Leonardo'],
    'Nota': [4, 7, 5.5, 9],
    'Aprovado': []
}

# for nota in alunos['Nota']:
#    if nota >= 6:
#        alunos['Aprovado'].append('Sim')
#    else:
#        alunos['Aprovado'].append('Não')

# Com map
# alunos['Aprovado'] = list(map(lambda nota: 'Sim' if nota >= 6 else 'Não', alunos['Nota']))

# Com list comprehension
alunos['Aprovado'] = ['\033[1;32mSim\033[m' if nota >= 6 else '\033[1;31mNão\033[m' for nota in alunos['Nota']]

dataframe = pd.DataFrame(alunos)
print(dataframe)

print()

obj1 = pd.Series([1, 6, 9, 3, 11])
print(obj1)

print()

array1 = np.array([23, 43, 2, 24, 4])
array2 = np.array([[2, 6, 9, 10, 5], [1, 43, 42, 5, 34434324]])
print(array1)
print(array2)

print()

obj2 = pd.Series(array1)
print(obj2)
