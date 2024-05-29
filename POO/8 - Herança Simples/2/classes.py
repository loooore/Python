class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def info(self):
        print(f'{self.nome} tem {self.idade} anos de idade')


class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome , idade)
        self.raca = raca

    def info(self):
        super().info()
        print(f'{self.nome} é um {self.raca}')
