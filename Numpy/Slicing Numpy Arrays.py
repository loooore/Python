import numpy as np

# Slicing Numpy Arrays
np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Return 2,3,4,5
print(np1[1:5])

# 4-9
print(np1[3:])

# Return negative Slices
# 7, 8
print(np1[-3:-1])

# Steps
print(np1[1:5])  # 2-5
print(np1[1:5:2])  # Will be print 2-5, with steps of 2

# Steps on the entire array
print(np1[::3])  # Will be print 1-9, with steps of 3

# Slice a 2d array
np2 = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
# Pull out a single item
print(np2[1, 2])

# Slice a 2d array 1-2
print(np2[0:1, 1:3])

# Slicing from rows 0-1, the items 1-2, 6-7
print(np2[0:2, 1:3])
