class Animal:
    def fazer_som(self):
        print("Som genérico de um animal")


class Cachorro(Animal):
    def fazer_som(self):  # Sobrescrita do método fazer_som
        print("Latido de cachorro")


cachorro = Cachorro()
cachorro.fazer_som()  # Saída: Latido de cachorro
