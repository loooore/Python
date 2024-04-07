import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_excel("C:/Users/l50038499/Desktop/pandas 1.xlsx")
dados.boxplot(column=['LT - Actual', 'Actual Period'])
plt.show()