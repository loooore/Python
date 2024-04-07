import numpy as np

# Search
np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3])

x = np.where(np1 == 3)
print(x)
print(x[0])
print(np1[x[0]])

for y in range(len(x[0])):
    print(x[0][y])

# Return even itens

y = np.where(np1 % 2 == 0)
print(f'The index: {y[0]} are even')