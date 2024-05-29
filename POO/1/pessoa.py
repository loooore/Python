from datetime import datetime


class Pessoa:
    ano_atual = int(datetime.strftime(datetime.now(), '%Y'))

    """
        __init__ - É o objeto construtor, utilizado para definir os atributos de um objeto
        self : Acessar os atributos e métodos do objeto usando self.nome_do_atributo ou self.nome_do_metodo().
               Torna as variáveis acessíveis em todo os objetos
    """

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome}, não pode falar comendo.')
            return

        if self.falando:
            print(f'{self.nome}, já está falando.')

        print(f'{self.nome}, está falando: {assunto}')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome}, não está falando.')
            return

        print(f'{self.nome}, parou de falar')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome}, já está comendo.')
            return  # Para a função aqui

        if self.falando:
            print(f'{self.nome}, não pode comer falando.')
            return

        print(f'{self.nome}, está comendo {alimento}')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return

        print(f'{self.nome}, parou de comer.')
        self.comendo = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
