import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('C:/Users/l50038499/Desktop/athlete_events.csv')
print(dados.head())


print(dados.keys())

# dados.hist(column=['Age', 'Height'], bins=20)
# plt.show()

age = dados['Age']
height = dados['Height']
print(f'Age: {age.head()}')
print(f'Height: {height.head()}')

plt.scatter(age, height)    # criando relação
plt.xlabel('Age')
plt.ylabel('Height')
plt.title('Scatter Plot: Age vs Height')
plt.grid(True)
plt.show()