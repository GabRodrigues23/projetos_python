# Faça um Programa que leia três números e mostre o maior e o menor deles.
'''
1. usuário deve informar 3 números distintos 
2. o sistema deverá analisar os 3 números e dizer o menor e o maior
3. deverão ser números inteiros
4. o sistema deverá imprimir o número maior e o menor
5. 
  input n1
  input n2
  input n3
  nmaior = n1
  if n2 > nmaior
    nmaior = n2
  if n3 > nmaior
    nmaior = n3
  print(nmaior)
  
  nmenor = n1
  if n2 < nmenor
    nmenor = n2
  if n3 < nmenor
    nmenor = n3
  print(nmenor)
 '''
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

nmaior = n1
if n2 > nmaior:
  nmaior = n2
if n3 > nmaior:
  nmaior = n3
print('{} é o número maior!'.format(nmaior))

nmenor = n1
if n2 < nmenor:
  nmenor = n2
if n3 < nmenor:
  nmenor = n3
print('{} é o número menor!'.format(nmenor))