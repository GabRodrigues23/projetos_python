print('Soma das frações de N')

N = int(input('Digite um número inteiro N: '))
H = 0

for i in range(1, N + 1):
    H += 1 / i

print(f'O valor de H é: {H}')