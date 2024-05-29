class Animal:
    @staticmethod
    def fazer_som():
        print("Som genérico de um animal")


class Cachorro(Animal):
    def fazer_som(self):
        print('latido de cachorro')


class Gato(Animal):
    def fazer_som(self):
        print('miado de gato')


def fazer_som(animais):
    for animal in animais:
        animal.fazer_som()