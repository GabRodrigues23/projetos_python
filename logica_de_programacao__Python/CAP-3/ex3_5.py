n = int(input('Digite um número: '))
fatorial = 1

if(n == 0):
    fatorial = 1
else:
    for i in range(1, n + 1):
        fatorial*= i

print(f'Fatorial de {n}: {fatorial}')

'''
def calcular_fatorial(numero):
    if numero == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, numero + 1):
            fatorial *= i
        return fatorial

# Solicita ao usuário para digitar um número inteiro
numero_usuario = int(input('Digite um número inteiro: '))

# Chama a função para calcular o fatorial e exibe o resultado
resultado_fatorial = calcular_fatorial(numero_usuario)
print(f'O fatorial de {numero_usuario} é: {resultado_fatorial}')

'''