import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv("C:/Users/l50038499/Desktop/athlete_events.csv")

homem_altura = []
homem_peso = []

# O zip está interando sexo, altura e peso em uma tupla: (M, 185.4, 89)
for sexo, altura, peso in zip(dados['Sex'], dados['Height'], dados['Weight']):
    if sexo == 'M':  # Verifica se o sexo é masculino ('M')
        if pd.isna(altura) or pd.isna(peso):  # Remove os valores nulos
            continue
        else:
            homem_altura.append(altura)
            homem_peso.append(peso)

# Criando uma relação entre a altura e o peso
plt.scatter(homem_altura, homem_peso)
plt.xlabel('Altura')
plt.ylabel('Peso')
plt.title('Altura x Peso de Homens')
plt.grid(True)
plt.show()
