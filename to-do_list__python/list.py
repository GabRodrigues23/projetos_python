import time

# Abre Lista - Define Valores Iniciais
print("-"*10,"To-Do List","-"*10)
open = True
lista = []

# Mostra Opções
while open == True:
    print("""O que deseja fazer?
[0] Fechar Lista
[1] Visualizar Lista
[2] Adicionar Item
[3] Remover Item
    """)
    
    # Recebe ação do usuário
    acao = int(input("> "))
    
    # Fecha a Lista de Tarefas
    if acao == 0:
        open = False
        print("Fechando lista.")
        time.sleep(1)
    
    # Exibe a Lista de Tarefas
    elif acao == 1:
        print(lista)
        time.sleep(1)
        print("\n")

    # Adiciona um Item na Lista de Tarefas
    elif acao == 2:
        adicionar = str(input("Digite a tarefa: ")) 
        time.sleep(1)
        lista.append(adicionar)
        print("\n")

    # Remove um Item da Lista de Tarefas
    elif acao == 3:
        # Verifica se há elementos na lista
        if lista:
            remover = int(input("Digite o elemento a ser removido: "))
            time.sleep(1)
            # Verifica se o índice corresponde à um item existente na lista
            if 0 <= remover < len(lista):
                lista.pop(remover)
                print("\n")
            # Caso o índice não corresponda ao item
            else:
                print("Índice inválido. Tente novamente!")
        #Caso não haja elementos na lista
        else:
            print("Não há elementos a serem removidos.")
            time.sleep(1)
            print("\n")

    # Caso Usuário digite um número inválidp
    else:
        print("Essa não é uma opção! Tente Novamente")
        time.sleep(1)
        print("\n")