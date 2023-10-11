def funcao_exemplo():
    print("Hello World!")

# Fora da Função
print("Este print será executado sempre que o módulo for importado.")
print(f"O valor de __name__ no módulo exemplo.py é: {__name__}")

if __name__ == "__main__":
    print("Este print só será executado se o arquivo exemplo.py for executado diretamente como programa.")
    funcao_exemplo()