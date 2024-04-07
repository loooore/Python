import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv("C:/Users/l50038499/Desktop/athlete_events.csv")

masculinos = dados.loc[dados['Sex'] == 'M']
altura = masculinos['Height']
peso = masculinos['Weight']

plt.scatter(altura, peso)
plt.show()
