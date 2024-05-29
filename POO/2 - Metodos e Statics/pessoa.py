from random import randint

class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento   # Só vai estar disponível dentro desse método
        return cls(nome, idade)

    @staticmethod # N precisa de instancia nem classe
    def gerar_id():
        rand = randint(1, 3)
        return rand