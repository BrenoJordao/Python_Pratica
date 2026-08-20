#CADASTRO DE JOGADORES POR NOME E PONTUAÇÃO!!!

jogadores = []# nossa lista de jogadores começa vazia...

def criacao_jogadores():
    nome = input('Qual o nome do jogador? ') 
    pontuacao = int(input('Qual a pontuação do jogador? '))

    jogador = { #Aqui ele atribui seus respectivos nomes e pontuações
        'nome': nome,
        'pontuacao': pontuacao
    }

    jogadores.append(jogador)#adicionando um novo jogador à nossa lista!!!

while True:

    dess = input('Deseja cadastrar um Jogador? [sim/nao] ')

    if dess == 'sim':#caso sim, chamamos nossa função de criação de jogadores
        criacao_jogadores()
        
    elif dess == 'nao':
        break

maior = jogadores[0]#maior pontuação começa com o jogador 0
menor = jogadores[0]#o mesmo se aplica pra menor

for x in jogadores:
    if x['pontuacao'] > maior['pontuacao']:
        maior = x
    #vamos conferir cada pontuação e atribuir a maior pontuação para nossa variável maior e a menor para a menor
    if x['pontuacao'] < menor['pontuacao']:
        menor = x


print(f'Seus jogadores: \n{jogadores}')
print(f'Jogador com maior pontuação: {maior['nome']} \n Jogador com menor pontuação: {menor['nome']}')
