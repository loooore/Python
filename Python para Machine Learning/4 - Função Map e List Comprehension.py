kmh = [40, 50, 55, 56, 40, 54, 324, 65, 120, 45]

mph = []
for i in kmh:
    mph.append(i / 1.61)
print(f' For - {mph}')


# Map - Com a função map deixa o código mais enxuto e mais leve
mph2 = list(map(lambda x: x / 1.61, kmh))
print(f' Map - {mph2}')
mph3 = map(lambda x: x / 1.61, kmh)
print(mph3)


# List Comprehension - Deixa o código ainda mais enxuto
mph4 = [x / 1.61 for x in kmh]
print(f' List Comprehension - {mph4}')

caracteres = [i for i in 'Lorenzo Toledol']  # Vai varrer cada um dos elementos dessa lista, e vai aplicar a função i
print(caracteres)
