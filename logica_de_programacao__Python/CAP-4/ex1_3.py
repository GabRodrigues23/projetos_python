from time import sleep
print('\nVetor 2\n')

tamanho_vetor = 5

vetor = []
for i in range(tamanho_vetor):
    valor = int(input(f'Digite o número da {i+1}° posição do vetor: '))
    vetor.append(valor)
    
procura = int(input('\nDigite o número que deseja procurar: '))
print(f'Procurando pelo número {procura}')
sleep(2)
print('.')

naoEncontrado = 0
for i in range(tamanho_vetor):
    if procura == vetor[i]: 
        print(f'O número {procura} está na posição {i+1} do vetor')
    else:
        naoEncontrado+= 1
        

if naoEncontrado == tamanho_vetor:
    print(f'O número {procura} não foi encontrado no vetor!')
elif tamanho_vetor - naoEncontrado == 1:
    print(f'O número {procura} foi encontrado {tamanho_vetor - naoEncontrado} vez no vetor')
else:
    print(f'O número {procura} foi encontrado {tamanho_vetor - naoEncontrado} vezes no vetor')
    
print('\n')