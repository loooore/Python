class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        desconto = (percentual / 100)
        self.preco -= self.preco * desconto
        print(f'Com o desconto de {desconto}, seu/sua {self.nome}, ficou {self.preco}')

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor.title()
        self._nome = valor.replace('a', '*')

    # Getter
    @property
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor
