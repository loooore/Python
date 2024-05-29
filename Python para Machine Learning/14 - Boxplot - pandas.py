import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('C:/Users/l50038499/Desktop/athlete_events.csv')
dados.boxplot(column=['Age', 'Height'])
plt.show()