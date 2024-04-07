import numpy as np

# 1-D
# np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# for x in np1:
#   print(x)

# 2-D Array
# np2 = np.array([[1,2,3,5], [5,6,7,8]])
# for x in np2:
#    for y in x:
#       print(y)

# 3-D array
np3 = np.array([[[1,2,3,4], [5,6,7,8]], [[9,10,11,12], [13,14,15,16]]])
# for x in np3:
#    print(x)
#    for y in x:
#        for z in y:
#            print(z)

# Use np.nditer()
for x in np.nditer(np3):
    print(x)
