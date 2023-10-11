# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

n1 = float(input('Digite o valor do primeiro produto: ').replace(',','.'))
n2 = float(input('Digite o valor do segundo produto: ').replace(',','.'))
n3 = float(input('Digite o valor do terceiro produto: ').replace(',','.'))

print('')

if n1 < n2 and n1 < n3:
  print('O primero produto é o mais barato!')
elif n2 < n1 and n2 < n3:
  print('O segundo produto é o mais barato!')
elif n3 < n1 and n3 < n2:
  print('O terceiro produto é o mais barato!')
elif n1 == n2 and n1 < n3:
  print('O primeiro e o segundo produto são os mais baratos!')
elif n1 == n3 and n1 < n2:
  print('O primeiro e o terceiro produto são os mais baratos!')
elif n2 == n3 and n2 < n1:
  print('O segundo e o terceiro produto são os mais baratos!')