from Classes import Cliente, Endereco

cliente1 = Cliente('Luiz', 32)
cliente1.inserir_enderecos('BSB', 'DF')

cliente2 = Cliente('Luiz 2', 32)
cliente2.inserir_enderecos('BSB', 'DF')

print(cliente1.nome)
cliente1.lista_enderecos()

print()

print(cliente2.nome)
cliente2.lista_enderecos()

del cliente2  # Apagaga o Luiz 2 e suas instancias

print()
print('- COLETOR DE LIXO! -' * 5)
print()

