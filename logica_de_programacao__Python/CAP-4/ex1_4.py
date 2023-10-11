print('\nVetor 3\n')

tamanho_vetor = 10

def le_vetor():
    vetor = []
    for i in range(tamanho_vetor):
        while True:
            try:
                valor = int(input(f"Digite o valor {i + 1} (entre 1 e 5): "))
                if 1 <= valor <= 5: # if valor >= 1 and valor <= 5
                    vetor.append(valor)
                    break
                else:
                    print("Por favor, digite um número entre 1 e 5.")
            except ValueError:
                print("Por favor, digite um valor inteiro entre 1 e 5.")
    return vetor

def calcula_distribuicao(vetor):
    distribuicao = [0] * 5
    for valor in vetor:
        distribuicao[valor - 1] += 1
    return distribuicao

def mostra_distribuicao(distribuicao):
    print("\nDistribuição de Frequência:")
    for i, quantidade in enumerate(distribuicao, start=1):
        print(f"Valor {i}: {quantidade} ocorrência(s))")

def main():
    print("Digite 10 valores inteiros entre 1 e 5.")
    vetor = le_vetor()
    distribuicao = calcula_distribuicao(vetor)
    mostra_distribuicao(distribuicao)

if __name__ == "__main__":
    main()