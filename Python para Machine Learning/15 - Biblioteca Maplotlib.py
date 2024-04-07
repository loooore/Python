import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

plt.scatter(x, y)   # Criando uma relação de X e Y
plt.show()


x1 = np.arange(0, 1000, 1)  # Arange cria um array de x a y, pulando de z em z
plt.plot(x1, -x1**3+7)
plt.show()
