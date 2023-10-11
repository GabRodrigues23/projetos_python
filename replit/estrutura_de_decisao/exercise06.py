# Faça um Programa que leia três números e mostre o maior deles.

n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
n3 = int(input('Digite o 3° número: '))

if n1 > n2 and n1 > n3:
  print('O primeiro número é maior!')
elif n2 > n1 and n2 > n3:
  print('O segundo número é maior!')
elif n3 > n1 and n3 > n2:
  print('O terceiro número é maior!')
else:
  print('Os número são iguais!')