dicio = {
    'Curso': 'Ciência da Computação',
    'Nome': 'Lorenzo',
    'Sobrenome': 'Toledo'
}

print(dicio['Nome'])

a = dicio['Curso']
print(a)

dicio['Curso'] = 'CCP'
print(dicio['Curso'])

dicio['Idade'] = 18
print(dicio)

print(dicio.keys())
print(dicio.values())
print(dicio.items())
