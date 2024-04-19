from pessoa import Pessoa

p1 = Pessoa('Lorenzo', 19)
p1.comer('maçã')
p1.comer('maçã')
p1.parar_comer()
p1.parar_comer()
p1.comer(1)
print()

p1.falar('Olá')
p1.parar_comer()
p1.falar('Olá galera')
p1.comer('cacto')
p1.parar_falar()
p1.comer('vidro')

print()
print('-'*100)
print()

p2 = Pessoa('Lucca', 21)
p3 = Pessoa('Arthur', 18)

p2.falar('Sou burro')
p3.falar('É msm')

p2.comer('vidro')
p3.parar_falar()
p3.comer('bolacha')

print()
print('-'*100)
print()

print(p1.ano_atual)
print(Pessoa.ano_atual)

print()
print('-'*100)
print()

print(f'{p1.nome} nasceu em {p1.get_ano_nascimento()}')