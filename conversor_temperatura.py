
def conversor_c():
    c = float(input('Quantos graus Celsius? '))
    f = c/5 *9 + 32
    print(f'{c}°C é igual a {f}°F')
    k = c + 273.15
    print(f'{c}°C é igual a {k}K')

def conversor_f():
    f = float(input('Quantos graus Fahrenheit? '))
    c = (f-32) /9 *5
    print(f'{f}°F é igual a {c}°C')
    k = (f-32) /9 *5 + 273.15
    print(f'{f}°F é igual a {k}K')

def conversor_k():
    k = float(input('Quantos graus Kelvin? '))
    c = k - 273.15
    print(f'{k}K é igual a {c}°C')
    f = (k-273.15) /5 *9 +32
    print(f'{k}K é igual a {f}°F')

print('Seja bem vindo(a) ao conversor de escalas termométricas!!!')
print('/'*50)

while True:

    decisao = int(input('Celsius(1) Fahrenheit(2) Kelvin(3)? '))

    if decisao == 1:
        conversor_c()

    elif decisao == 2:
        conversor_f()

    elif decisao == 3:
        conversor_k()

    else:
        print('Resposta inválida')

    print('/'*50)

