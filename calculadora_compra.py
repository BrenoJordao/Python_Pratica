#Confeço que esse foi bem mais simples...

#pergunta sobre o produto
valor = float(input('Qual o valor do produto? '))
#quantos produtos?
qtd = int(input('Quantos produtos comprou? '))

def calcular_compra(): #vamos calcular se ele tem direito a descontos
    p = valor*qtd
    if p > 100:#se passar de 100, ele tem 10% de desconto
        p1 = p - p*0.1
        print(f'total da compra R${p} você tem 10% de desconto, sua compra ficou por R${p1}')

    elif p >= 50:#se passar de 50, tem 5% de desconto
        p2 = p - p*0.05
        print(f'total da compra R${p} você tem 5% de desconto, sua compra ficou por R${p2}')

    else:#caso seja abaixo de 50, ele nao tem desconto
        print(f'total da compra R${p}')

calcular_compra()#haja-se a luz!

    