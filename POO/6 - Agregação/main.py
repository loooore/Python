from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

p1 = Produto('Camisete', 40)
p2 = Produto('Apple Vision Pro', 20000)
p3 = Produto('S24 Ultra', 8000)

carrinho.inserir_produtos(p1, p2, p3, p2, p1, p2, p3)
carrinho.lista_produtos()
print(carrinho.soma_total())