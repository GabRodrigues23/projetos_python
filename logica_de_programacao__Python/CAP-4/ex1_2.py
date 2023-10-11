print('\nVetores\n')

# Define a quantidade de indicies que entrarão nos vetores a partir do laço for
tamanho_vetor = 20

# Leitura do primeiro vetor
vet1 = []
for i in range(tamanho_vetor):
    valor = int(input(f'Digite o valor do {i+1}° índice do 1° vetor: '))
    vet1.append(valor)

print('\n')

# Leitura do segundo vetor
vet2 = []
for i in range(tamanho_vetor):
    valor = int(input(f'Digite o valor do {i+1}° índice do 2° vetor: '))
    vet2.append(valor)

print('\n')

# Leitura do vetor de operacoes
vet_operacoes = []
for i in range(tamanho_vetor):
    operacao = input(f"Digite a operação do {i+1}° índice: ")
    while operacao not in ['+', '-', '*', '/']:
        print("Operação inválida. Digite uma das seguintes operações: +, -, *, /")
        operacao = input(f"Digite a operação do {i+1}° índice: ")
    vet_operacoes.append(operacao)

print('\n')

# Realização das operações e armazenamento dos resultados no quarto vetor
vet_resultado = []
for i in range(tamanho_vetor):
    if operacao == '+':
        resultado = vet1[i] + vet2[i]
    elif operacao == '-':
        resultado = vet1[i] - vet2[i]
    elif operacao == '*':
        resultado = vet1[i] * vet2[i]
    elif operacao == '/':
        resultado = vet1[i] / vet2[i]
    vet_resultado.append(resultado)

print('\n')

# Mostrar todos os vetores
print('Primeiro vetor: ', vet1)
print('Segundo vetor: ', vet2)
print('Operações: ', vet_operacoes)
print('Resultado das operações: ', vet_resultado)