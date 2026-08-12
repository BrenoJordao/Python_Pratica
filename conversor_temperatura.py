#CONVERSOR DE ESCALAS TERMOMÉTRICAS !!!

def conversor_c(): #Conversor usando Celsius como base
    c = float(input('Quantos graus Celsius? '))
    f = c/5 *9 + 32
    print(f'{c}°C é igual a {f}°F')
    k = c + 273.15
    print(f'{c}°C é igual a {k}K')

def conversor_f(): #Conversor usando Fahrenheit como base
    f = float(input('Quantos graus Fahrenheit? '))
    c = (f-32) /9 *5
    print(f'{f}°F é igual a {c}°C')
    k = (f-32) /9 *5 + 273.15
    print(f'{f}°F é igual a {k}K')

def conversor_k(): #Conversor usando Kelvin como base
    k = float(input('Quantos graus Kelvin? '))
    c = k - 273.15
    print(f'{k}K é igual a {c}°C')
    f = (k-273.15) /5 *9 +32
    print(f'{k}K é igual a {f}°F')

print('Seja bem vindo(a) ao conversor de escalas termométricas!!!') #Boas vindas nunca é demais
print('/'*50)

while True:

    decisao = int(input('Celsius(1) Fahrenheit(2) Kelvin(3)? ')) #Vamos trabalhar com qual escala?

    if decisao == 1: #escolhendo 1
        conversor_c() #chame nosso conversor de Celsius!

    elif decisao == 2: #escolhendo 2
        conversor_f() #chame nosso conversor de Fahrenheit!

    elif decisao == 3: #escolhendo 3
        conversor_k() #chame nosso conversor de Kelvin

    else: #caso nao escolha nada:
        print('Resposta inválida')

    print('/'*50)

