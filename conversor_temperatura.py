
def conversor(c):
    f = c/5 *9 + 32
    print(f'{c}°C é igual a {f}°F')
    k = c + 273.15
    print(f'{c}°C é igual a {k}K')

print('Seja bem vindo(a) ao conversor de Celsius para outras escalas!!!')
print('/'*50)

while True:

    c = float(input('Quantos graus Celsius? '))
        
    conversor(c)

