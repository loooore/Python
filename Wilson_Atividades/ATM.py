import random
from time import sleep
from sys import exit

# Variaveis goblais
usuario = {}
random_num = random.randint(3, 10)


def usuario_login():
    while True:
        nome = (input('Informe seu nome: ')).lower().title()
        if not nome.isalpha():
            print('[ERROR] - Valor inválido!')
        else:
            usuario['Nome'] = nome
            break
    while True:
        try:
            usuario['Saldo'] = float(input('Informe seu saldo: '))
            break
        except ValueError:
            print('[ERROR] - Saldo inválido!')
    usuario['Numero_Conta'] = random.randint(10000, 99999)


def menu_conta():
    print("----------------------------------------")
    print("|                                      |")
    print("|       1   -   Conta Corrente         |")
    print("|       2   -   Conta Poupança         |")
    print("|       3   -   Conta Universitária    |")
    print("|       4   -   Conta Salário          |")
    print("|       5   -   Cancelar Operacao      |")
    print("|                                      |")
    print("----------------------------------------")


def usuario_msg(tipo_conta):
    print('-' * 38)
    print(f'{"|".ljust(37)}|')
    print(f'| Conta {tipo_conta} aberta com sucesso! |')
    print(f'| Nome: {usuario.get("Nome", "").ljust(29)}|')
    print(f'| Saldo: R${usuario.get("Saldo", 0.00)} '.ljust(37) + '|')
    print(f'| Número da Conta: {usuario.get("Numero_Conta", "")} '.ljust(37) + '|')
    print(f'{"|".ljust(37)}|')
    print('-' * 38)


def switch_menu_conta(opcao_conta):
    tipo_conta = {
        1: 'Corrente',
        2: 'Poupança',
        3: 'Universitária',
        4: 'Salário'
    }
    if opcao_conta in tipo_conta:
        tipo_conta = tipo_conta[opcao_conta]
        usuario_msg(tipo_conta)


def operacoes_menu():
    print("---------------------------------------")
    print("|                                     |")
    print("|       1   -   Consultar Saldo       |")
    print("|       2   -   Depositar Valor       |")
    print("|       3   -   Sacar Valor           |")
    print("|       4   -   Sair                  |")
    print("|                                     |")
    print("---------------------------------------")


def switch_menu_saldo(opcao):
    if opcao == 1:
        consultar_saldo()
    elif opcao == 2:
        depositar_saldo()
    elif opcao == 3:
        sacar_saldo()


def consultar_saldo():
    print('Consultando', end='')
    for i in range(random_num):
        print('.', end='')
        sleep(1)
    msg_saldo()


def depositar_saldo():
    while True:
        try:
            saldo_depositado = float(input('Informe quantos reais deseja depositar: '))
            if saldo_depositado <= 0:
                print('[ERROR] - Valor de depósito inválido! O valor deve ser positivo.')
            else:
                usuario['Saldo'] += saldo_depositado
                print('Depositando', end='')
                for i in range(random_num):
                    print('.', end='')
                    sleep(1)
                msg_saldo()
                break
        except ValueError:
            print('[ERROR] - Valor inválido! Por favor, insira um valor numérico.')


def sacar_saldo():
    while True:
        try:
            saque = float(input('Informe quantos reais deseja sacar: '))
            if saque <= 0:
                print('[ERROR] - Valor de saque inválido! O valor deve ser positivo.')
            elif saque > usuario['Saldo']:
                print('[ERROR] - Saldo insuficiente para saque.')
            else:
                print('Sacando', end='')
                for _ in range(random_num):
                    print('.', end='')
                    sleep(1)
                usuario['Saldo'] -= saque
                msg_saldo()
                break
        except ValueError:
            print('[ERROR] - Valor inválido! Por favor, insira um valor numérico.')


def msg_saldo():
    print('\n' + '-' * 38)
    print(f'{"|".ljust(37)}|')
    print(f'| Seu saldo atual é: R${usuario.get("Saldo", 0.00)} '.ljust(37) + '|')
    print(f'{"|".ljust(37)}|')
    print('-' * 38)


def msg_fim():
    print('\n' + '-' * 41)
    print(f'{"|".ljust(40)}|')
    print(f'| Obrigado por utilizar nossos serviços '.ljust(38) + '|')
    print(f'{"|".ljust(40)}|')
    print('-' * 41)
    exit()


# Main
menu_conta()
while True:
    try:
        opccao_conta = int(input('Informe qual conta deseja criar: '))
        if opccao_conta < 1 or opccao_conta > 5:
            print('Operação inválida')
        elif opccao_conta == 5:
            msg_fim()
        else:
            break
    except ValueError:
        print('[ERROR] - Operação inválida!')

usuario_login()
switch_menu_conta(opccao_conta)

while True:
    operacoes_menu()
    try:
        opcao_saldo = int(input('Informe qual operação deseja fazer: '))
        if opcao_saldo < 1 or opcao_saldo > 4:
            print('[ERROR] - Opção não implementada!')
        elif opcao_saldo == 4:
            msg_fim()
        else:
            switch_menu_saldo(opcao_saldo)
    except ValueError:
        print('[ERROR] - Operação inválida!')
