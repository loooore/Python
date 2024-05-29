class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produtos(self, *produtos):
        for produto in produtos:
            self.produtos.append(produto)

    def lista_produtos(self):
        print('O seu carrinho de compras contém: ', end='')
        for produto in self.produtos:
            if produto == self.produtos[-1]:
                print(produto.nome)
            else:
                print(produto.nome, end=', ')

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
