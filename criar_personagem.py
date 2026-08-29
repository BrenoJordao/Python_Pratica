#BEM VINDOS À CRIAÇÃO DE PERSONAGENS MAIS SEM GRAÇA DO MUNDO!!!

#meu segundo código com poo, então foi só praa treinar mesmo.abs

#aqui criamos nossa classe de personagem
class Personagem:
    #ele recebe nome, vida e ataque
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    #um método pra ele mostrar os status do player
    def status(self):
        return f'{self.nome}, HP: {self.vida}, ataque: {self.ataque}'

    #se ele quiser atacar outro player, ele consegue
    def atacar(self, alguem):
        alguem.vida -= self.ataque

    
#criei dois onjetos de players pra testar
player1 = Personagem('Gandalf', 100, 30) 
player2 = Personagem('Thorin', 80, 20)
#mostro os status dos players
print(player1.status())
print(player2.status())
#Gandalf ataca Thorin
player1.atacar(player2)
#mostro status de Thorin, depois de ser atacado
print(player2.status())


