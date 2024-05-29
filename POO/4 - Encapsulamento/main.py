"""
Public +
Private -
Protected #
Package ~

_ - 1 underline antes do atributo/metodo, (public, um pouco mais restrito)
__ - 2 underline antes do atributo/metodo, private
"""


class BaseDados:
    def __init__(self):     # Como o init é public, é possível alterar o valor de dados no main, quebrando o código
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


bd = BaseDados()
bd.inserir_cliente(1, 'Lorenzo')
bd.inserir_cliente(2, 'Lucca')
bd.inserir_cliente(3, 'Arthur')
bd.apaga_cliente(2)
bd.lista_clientes()
bd.__dados = 'Outrra Coisa' # Cria um novo atributo
print(bd.__dados)
print(bd._BaseDados__dados)
print(bd.dados)
bd.dados = 'Outro Valor'

print('-'* 50)