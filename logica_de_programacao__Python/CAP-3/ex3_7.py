print('\nMaior e Menor!')

contador = 1

for i in range(1,20):
    num = int(input('Digite um número: '))
    if(contador == 1):
        menor = num
        maior = num
        contador+= 1
    if(num > maior):
        maior = num
    else:
        maior = maior
    if(num < menor):
        menor = num
    else:
        menor = menor
print(f'Maior: {maior}\nMenor: {menor}')