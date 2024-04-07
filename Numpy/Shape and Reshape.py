import numpy as np
# Create a 1-D Numpy Array and Get Shape
np1 = np.array([1, 2, 3, 4, 5, 6 ,7, 8, 9, 10, 11, 12])
print(np1)
print(np1.shape)

# Create a 2-D Array and get Sha´pe, (rows/columns)
# np2 = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])
# print(np2)
# print(np2.shape)
# (2, 6)

# Reshape 2-D
# np3 = np1.reshape(3, 4)
# print(np3)
# print(np3.reshape())

# Reshape 3-D
np4 = np1.reshape(2, 3, 2)
print(np4)
print(np4.shape)

# Flatten to 1-D
np5 = np4.reshape(-1)
print(np5)
print(np5.shape)
