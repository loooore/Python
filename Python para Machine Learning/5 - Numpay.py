import numpy as np

# 1D
a = np.array([1, 2, 3])
print(a)
print()

# 2D
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print()

# 3D
c = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [[9, 10, 11, 12], [13, 14, 15, 16]]])
print(c)
print()

# Zeros
d = np.zeros((4, 3))
print(d)
print()

# Ones
e = np.ones((4, 3))
print(e)
print()

# Msm dimensões de linhas e colunas
f = np.eye(5)
print(f)
print()

# Max/Min
print(b.max())
print(b.min())
print()

# Sum / Média / Desvio padrão
print(b.sum())
print(b.mean())
print(b.std())
