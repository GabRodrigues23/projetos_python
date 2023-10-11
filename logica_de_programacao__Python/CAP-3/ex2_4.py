print("\nPeso ideal!")

print(
'''[1] Homem
[2] Mulher''')
sexo = int(input('Digite seu sexo: '))
altura = float(input('Digite sua altura: '))

if(sexo == 1):
    ideal = (72.7 * altura) - 58
else:
    ideal = (62.1 * altura) - 44.7

print(f'O peso ideal para sua altura é: {ideal:.2f}Kg');