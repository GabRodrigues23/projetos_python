print('\nIdentificador de números primos!')

num = int(input('Digite um número: '))
div = 0

for i in range(1, num + 1):
    if num % i == 0:
        div += 1

if div == 2 or div == 1:
    print('É primo!')
else:
    print('Não é primo!')
