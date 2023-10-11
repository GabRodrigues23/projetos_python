print('\nCódigo de Produto!')

cod = int(input('Digite o código do produto: '))

if(cod == 1):
    print('Alimento não perecível')
elif(cod >= 2 and cod <= 4):
    print('Alimento perecível')
elif(cod == 5 or cod == 6):
    print('Vestuário')
elif(cod == 7):
    print('Higiene Pessoal')
elif(cod >= 8 and cod <= 15):
    print('Limpeza e utensílios domésticos')
else:
    print('Inválido')