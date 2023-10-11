# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:                                        o produto do dobro do primeiro com metade do segundo .        a soma do triplo do primeiro com o terceiro.                  o terceiro elevado ao cubo.

n1 = float(input('Digite o primeiro número inteiro: ').replace(',','.'))
n2 = float(input('Digite o segundo número inteiro: ').replace(',','.'))
nr = float(input('Digite um número real: ').replace(',','.'))
produto = (n1 * 2) * (n2 / 2)
soma = (n1 * 3) * nr
elevado = nr * nr * nr
print('1. {:.0f}'.format(produto))
print('2. {:.0f}'.format(soma))
print('3. {:.2f}'.format(elevado))