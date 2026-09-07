
class Produto: #nosso produto terá nome, preço e estoque
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def __str__(self): #podemos dar um print no obj pra ele mostrar essas informações
        return f'Produto: {self.nome}\nPreço: R${self.preco}\nEstoque: {self.estoque}'

    def vender(self, venda): #para vender, precisamos saber se tem estoque pra isso
        if self.estoque >= venda:
            self.estoque -= venda
            return f'{venda} foram vendidos de {self.nome}'
        
        else:
            return f'Venda indisponível para a quantidade escolhida!'

    def repor(self, repondo): #aqui ele adiciona estoque ao produto
        self.estoque += repondo
        return f'{repondo} foram adicionados ao estoque de {self.nome}'

p1 = Produto('cocozinho', 3.99, 5)
print(p1)

print(p1.vender(7))
print(p1.repor(10))
print(p1.vender(7))

print(p1)


