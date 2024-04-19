import random

def menu_conta(tipo_conta):
    print("----------------------------------------")
    print("|                                      |")
    print("|       1   -   Conta Corrente         |")
    print("|       2   -   Conta Poupanca         |")
    print("|       3   -   Conta Universitaria    |")
    print("|       4   -   Conta Salario          |")
    print("|       5   -   Cancelar Operacao      |")
    print("|                                      |")
    print("----------------------------------------")
    while True:
        try:
            tipo_conta = int(input('Informe o tipo de conta que deseja criar: '))
        except ValueError:
            print('[ERROR] - Operação inválida!')
        else:
            usuario['Nome'].append(input('Informe seu nome: '))
            while True:
                try:
                    usuario['Saldo'].append(int(input('Informe seu saldo: ')))
                    break
                except ValueError:
                    print('[ERROR] - Saldo inválido!')
            usuario['Numero_Conta'].append(random.randint(10000000, 9999999))

usuario = {
    'Nome': [],
    'Saldo': [],
    'Numero_Conta': [],
    'Conta': []
}
print(menu_conta(1))
print(usuario)

