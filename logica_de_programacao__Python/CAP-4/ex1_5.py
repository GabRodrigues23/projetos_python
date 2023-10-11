print('\nVetor 4\n')

# Leitura do vetor
def le_vetor(tamanho_vetor):
    vetor = []
    for i in range(tamanho_vetor):
        valor = int(input(f'Digite o valor {i+1} do vetor: '))
        vetor.append(valor)
    return vetor

# Leitura da ordenação do vetor
def bubbleSort(vetor):
    # Define o tamanho do vetor de acordo com a quantidade dentro do vetor, para ser utilizado no laço for
    tamanho_vetor = len(vetor)
    # Ordena o vetor em ordem crescente
    for i in range(tamanho_vetor):
        for j in range(0, tamanho_vetor-i-1):
            if vetor[j] > vetor[j+1]:
                # Trocar os elementos de posição se estiverem na ordem errada
                vetor[j], vetor[j+1] = vetor[j+1], vetor[j]

# Imprime os valores do vetor e o ordena
def main():
    tamanho_vetor = 5
    vetor = le_vetor(tamanho_vetor)
    print("Vetor original:", vetor)

    bubbleSort(vetor)

    print("Vetor ordenado em ordem crescente:", vetor)

main()