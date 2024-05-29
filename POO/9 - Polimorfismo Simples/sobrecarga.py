class Calculadora:
    def somar(self, a, b):  # Método com dois parâmetros
        return a + b

    def somar(self, a, b, c):  # Método com três parâmetros (simulação de sobrecarga)
        return a + b + c


calc = Calculadora()
# print(calc.somar(2, 3))      # Erro! Não há método somar com dois argumentos definido.
print(calc.somar(2, 3, 4))   # Saída: 9
