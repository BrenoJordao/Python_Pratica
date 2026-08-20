#BEM VINDOS À SUA LISTA DE COMPRAS!!!
produtos = []#começamos com a lista vazia, pois nao há produtos

total = 0 #total da compra começa com zero

def cadastrar(): #Criando nosso produto
    nome = input('Nome do produto: ')
    preco = float(input('Preço do produto: R$'))

    add = {'produto': nome, 'preço': preco} #colocando nosso produto num dicionário

    produtos.append(add)#Adicionando o dicionário à lista

while True:#cadastre quantos produtos quiser
    quer = input('Deseja cadastrar um Produto?[sim/nao] ')

    if quer == 'sim':
        cadastrar()

    elif quer == 'nao':
        break

caro = produtos[0]#produto mais caro
barato = produtos[0]#mais barato

for x in produtos:#confere cada produto da lista
    total += x['preço']#soma todos os preços

    if x['preço'] > caro['preço']:#conferindo qual o mis caro
        caro = x

    if x['preço'] < barato['preço']:#conferindo o mais barato
        barato = x

print(f'Produtos cadastrados: \n {produtos}')
print(f'Produto mais caro: {caro}')
print(f'Produto mais barato: {barato}')
print(f'Total da compra R${total}')