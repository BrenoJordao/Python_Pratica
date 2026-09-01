#BEM VINDOS À CARTEIRA DIGITAL!!!

#pra começar, eu ainda tô aprendendo poo, então não esperem algo muito hard

class Conta:  #classe da conta
    def __init__(self, nome): #precisamos de nome, e o saldo começa com zero
        self.nome = nome
        self.saldo = 0

    def depositar(self): #quanto você quer depositar?
        deposito = float(input('De quanto será seu depósito? R$'))
        self.saldo += deposito
        print(f'Saldo atual R${self.saldo}')

    def sacar(self): #quanto quer sacar?
        saque = float(input('De quanto será seu saque? R$'))
        if saque <= self.saldo:
            print(f'Saque de R${saque} realizado com sucesso!')
            self.saldo -= saque

        else: #se tentar tirar mais do que tem, nao deixo!
            print('Saldo insuficiente!')

    def __str__(self): #status da conta
        return f'Conta de {self.nome} com saldo de R${self.saldo}'

#criei um objeto da classe conta!
conta1 = Conta('Jordan')

while True:#loop easy pra você escolher o que quer fazer no programa
    escolha = int(input('Faça sua escolha:\n1 Status da conta\n2 Depositar\n3 Sacar\n4 Sair\nresposta>>>'))

    if escolha == 1:
        print(conta1)

    elif escolha == 2:
        conta1.depositar()

    elif escolha == 3:
        conta1.sacar()

    elif escolha == 4:
        print('Saindo...')
        break

    else:
        print('mensagem inválida!')

