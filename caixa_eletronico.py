#BEM VINDOS AO CAIXA ELETRÔNICO!!!

saldo = 1000.00 #começamos com um saldo de 1000 reais

def consultar_saldo(): #caso o usuário queira ver se sobrou grana pros boletos
    print(f'Seu saldo atual R${saldo}')
    print('/'*50)

def depositar(): #vamos depositar a graninha dos bicos que o usuário fez
    global saldo #para manipularmos essa variável, precisamos declará-la como global
    dpst = float(input('Quanto você deseja depositar? R$'))
    saldo += dpst #depósito é adicionado ao saldo
    print('/'*50)

def sacar(): #o usuário quer se endividar
    global saldo #mesma explicação anterior, precisa ser global para ser manipulada
    saque = float(input('Quanto você deseja sacar? R$'))

    if saque <= saldo: #se tiver saldo suficiente, ele subtrai o saque do saldo
        print(f'Você sacou R${saque}!')
        saldo -= saque
        print('/'*50)

    else: #caso ele seja guloso e queira sacar mais do que tem, o programa nao deixa
        print('Saldo insuficiente!')
        print('/'*50)


while True:
    print('===== CAIXA ELETRÔNICO =====')
    #aqui vamos saber o que o usuário quer:
    escolha = int(input('1 - consultar saldo\n2 - depositar\n3 - sacar\n4 - sair\n'))

    #essa parte está autoexplicativa, bem legível:
    if escolha == 1: 
        consultar_saldo()
    
    elif escolha == 2:
        depositar()

    elif escolha == 3:
        sacar()

    elif escolha == 4:
        print('/'*50)
        print('Fechando...')
        break

    #sim, se ele digitar uma string, por exemplo, o código quebra. Mas acho que nao devo me preocupar com isso agora
    else:
        print('Entrada inválida!')