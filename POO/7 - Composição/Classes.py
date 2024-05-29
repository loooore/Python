class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def inserir_enderecos(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        for endeco in self.enderecos:
            print(endeco.cidade, endeco.estado)

    def __del__(self):
        print(f'{self.nome} foi apagado!')


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.cidade} / {self.estado} foi apagado!')
