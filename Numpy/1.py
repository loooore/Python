import numpy as np

np1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(np1)
print(np1.shape)

print()

# Range
np2 = np.arange(11)
for n in np2:
    if n == np2[-1]:
        print(n)
    else:
        print(n, end=', ')
print(np2)

print()

# Step
np3 = np.arange(0, 10, 2)
print(np3)

print()

# Zeros
np4 = np.zeros(10)
print(np4)

print()

# Multidimensional zeros
np5 = np.zeros((2,10))
print(np5)

print()

# Full
np6 = np.full(10, 6)
print(np6)

print()

# Multidimensional Full
np7 = np.full((2,10), 6)
print(np7)

print()

# Convert Python list to np
my_list = [1, 2, 3, 4, 5]
np8 = np.array(my_list)
print(np8)