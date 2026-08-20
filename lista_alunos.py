#Esse código é só eu testando loops, nada de legal...

notas = [2,3,4,5,6,7,8,9,10]
media = 0
maior = notas[0]
menor = notas[0]

print('A seguir, suas notas:')

for x in notas:
    print(x)

for x in notas:
    media += x

print(f'média: {media/len(notas)}')

for x in notas:
   if x > maior:
    maior = x

print(f'Maior nota: {maior}')

for x in notas:
    if x < menor:
        menor = x
    

print(f'Menor nota: {menor}')


print('Notas na média:')
for x in notas:
    if x >= 6:
        print(x)

    
    
