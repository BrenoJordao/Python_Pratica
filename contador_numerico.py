# BEM VINDOS AO CONTADOR NUMÉRICO !!!

n = [] #todos os números que serão armazenados
quantia = 0 #total de números da lista
soma = 0 #soma de toda a lista
posi = 0 #se há positivos
nega = 0 #se há negativos
media = 0 #nossa média

while True: #sempre vai repetir nosso contador, até o usuário cansar

    while True: #loop para cadastrar números
        
        numero = int(input('Digite um número, se quiser parar, digite 0: '))
        if numero == 0 and n == []: #se o usuário nao adicionar números, então reseta a pergunta!
            print('Você precisa digitar algum valor!')
            continue


        if numero != 0: #enquanto ele adiciona números, vai guardando na nossa lista n
            n.append(numero)
            quantia += 1 #a cada numero adicionado, mais 1 será guardado em nossa quantidade total

        else: #quando o usuario para de cadastrar numeros, esse loop de acaba
            break

    for x in n: #vamos conferir umas coisinhas em nossos numeros
        
        soma += x #ele vai somar todos os numeros que cadastramos

        if x > 0: #confere se há positivos
            posi += 1

        else: #confere se há negativos
            nega += 1

    if n != []: 
        media = soma/quantia #calculando a média

        #nossos queridos resultados !!!
        print('/'*50)
        print(f'você digitou {quantia} números, sendo eles: {n}')
        print(f'Existem {posi} números positivos e {nega} numeros negativos')
        print(f'A média dos números é {media}')

    continuando = input('Você quer continuar? [sim/nao]: ')#quer continuar?

    if continuando == 'nao': #se nao quiser continuar, entao pare!
        break

    elif continuando == 'sim': #se quiser continuar, resete nossos valores !!!
        n = []
        quantia = 0
        soma = 0
        posi = 0
        nega = 0
        media = 0

