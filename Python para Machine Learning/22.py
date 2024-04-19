import keras
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
df = pd.read_csv('c:/Users/l50038499/Downloads/admission_dataset (1).csv')
df
y = df['Chance of Admit ']
x = df.drop('Chance of Admit ', axis=1)

x_treino, x_teste = x[0:300], x[300:]
y_treino, y_teste = y[0:300], y[300:]

from keras.models import Sequential
from keras.layers import Dense

# Criando a arquitetura da rede neural:

modelo = Sequential()   # Serve pra add camadas sequencialmente
modelo.add(Dense(units=3, activation='relu', input_dim=x_treino.shape[1]))
modelo.add(Dense(units=1, activation='linear'))

# treinando a rede neural

modelo.compile(loss='mse', optimizer='adam', metrics=['mae'])
resultado = modelo.fit(x_treino, y_treino, epochs=200, batch_size=32, validation_data=(x_teste, y_teste))

import matplotlib.pyplot as plt

plt.plot(resultado.history['loss'])
plt.plot(resultado.history['val_loss'])
plt.title('Histórico de Treinamento')
plt.ylabel('Função de custo')
plt.xlabel('Épocas de Treinamento')
plt.legend(['Erro Treino', 'Erro teste'])
plt.show()