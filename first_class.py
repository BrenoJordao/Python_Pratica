#MEUS PRIMEIROS CÓDIGOS COM POO!!!

#é só tirar essas aspas(''') pra rodar esse código abaixo.

'''class Seila: 
    def __init__(self):
        self.nome = ' '
        self.idade = 0

    def se(self):
        resp =  input(f'{self.nome} completa aniversario? [s/n] ')
    
        if resp == 's':
            self.idade += 1


    def mensagem(self):
        return f'{self.nome} é estudante e tem {self.idade} anos!!!'


g1 = Seila()
g1.nome = input('Qual seu nome: ')
g1.idade = int(input('qual sua idade: '))
g1.se()
print(g1.mensagem()) '''


class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def __str__(self):
        return f'Olá, me chamo {self.nome}, meu setor é de {self.setor} e meu cargo: {self.cargo}!'

funcionario1 = Funcionario('Jordan','TI','programador')
print(funcionario1)

