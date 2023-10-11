print('\nAno de nascimento!')

anoNasc = int(input('Digite o ano que você nasceu: '))
idade = (2023 - anoNasc)
#print(idade)
if(idade >= 18):
    print('Você ja pode tirar a carteira de habilitação!')
elif(idade >= 16 and idade < 18):
    print('Você ja tem idade para votar!')
else:
    print('Você ainda não pode votar nem tirar a carteira de habilitação!')