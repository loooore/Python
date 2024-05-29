from pessoa import Pessoa

#   p1 = Pessoa.por_ano_nascimento('Lorenzo', 2005)
p1 = Pessoa('Lorenzo', 19)
print(p1.nome, p1.idade)
p1.get_ano_nascimento()
print(Pessoa.gerar_id())
