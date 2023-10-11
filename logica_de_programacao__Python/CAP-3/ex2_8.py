print('Desconto em produtos')

prod = float(input('Digite o valor do produto: '))
print('''
    [1] À vista em dinheiro
    [2] Cheque
    [3] À vista no cartão de crédito
    [4] 2 vezes
    [5] 3 vezes
''')
pag = int(input('Escolha a forma de pagamento: '))

if(pag == 1 or pag == 2):
    #10% de desconto
    desc = prod * 0.10
    prod-= desc
    print(f'Você recebeu um desconto de 10%\nSua compra ficou em R${prod:.2f}')
elif(pag == 3):
    #5% de desconto
    desc = prod * 0.05
    prod-= desc
    print(f'Você recebeu um desconto de 5%\nSua compra ficou em R${prod:.2f}')
elif(pag == 4):
    #sem desconto
    print(f'Sua compra ficou em R${prod:.2f}')
elif(pag == 5):
    #juros de 10%
    jur = prod * 0.10
    prod+= jur
    print(f'Acrescentando 10% de juros da máquina\nSua compra ficou em R${prod:.2f}')
else:
    print('Forma de pagamento inválida')