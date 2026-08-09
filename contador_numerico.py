
n = []
quantia = 0
soma = 0
posi = 0
nega = 0
media = 0

while True:

    while True:
        
        numero = int(input('Digite um número, se quiser parar, digite 0: '))
        if numero == 0 and n == []:
            print('Você precisa digitar algum valor!')
            continue


        if numero != 0:
            n.append(numero)
            quantia += 1

        else:
            break

    for x in n:
        
        soma += x

        if x > 0:
            posi += 1

        else:
            nega += 1

    if n != []:
        media = soma/quantia


    if n != []:
        print('/'*50)
        print(f'você digitou {quantia} números, sendo eles: {n}')
        print(f'Existem {posi} números positivos e {nega} numeros negativos')
        print(f'A média dos números é {media}')

    continuando = input('Você quer continuar? [sim/nao]: ')

    if continuando == 'nao':
        break

    else:
        n = []
        quantia = 0
        soma = 0
        posi = 0
        nega = 0
        media = 0

