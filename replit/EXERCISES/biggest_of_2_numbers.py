# Faça um Programa que peça dois números e imprima o maior deles.

'''
1. usuario deve informar dois numeros
2. comparar os dois numeros e imprimir o maior
3. -
4. o programa devera imprimir o numero maior
5. 
input n1
input n2
if n1 > n2
  print n1
if n2 > n1
  print n2
'''
n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
if n1 > n2:
  print(n1,'é o número maior!')
else:
  print(n2, 'é o número maior!')