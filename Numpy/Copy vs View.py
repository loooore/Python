import numpy as np

# Copy vc View
np1 = np.array([0, 1, 2, 3, 4, 5])

'''# Create a view
np2 = np1.view()

print(f'Original Np1 {np1}')
print(f'Original Np2 {np2}')

np1[0] = 42
print(f'Changed Np1 {np1}')
print(f'Original Np2 {np2}')'''


# Create a copy
np2 = np1.copy()

print(f'Original Np1 {np1}')
print(f'Original Np2 {np2}')

np1[0] = 42
print(f'Changed Np1 {np1}')
print(f'Original Np2 {np2}')

np2[3] = 123
print(f'Changed NP2 {np2}')