def somaQu(a=1, b=1):
    somaQ = a ** 2 + b ** 2
    return somaQ


print(somaQu(3, 6))

# Função lambda é chamada de função anônima
somaQu2 = lambda a=1, b=1: a ** 2 + b ** 2
print(somaQu2(3, 6))

