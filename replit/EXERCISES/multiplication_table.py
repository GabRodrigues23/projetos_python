# Faça um programa em Python que leia um valor inteiro e mostre a tabuada de 1 a 10 do valor lido.

'''
1. usuario deve informar um numero
2. imprimir a tabuada do numero informado
3. devera ser um numero inteiro
4. o usuario deve informar um numero e o sistema irá imprimir a tabuada desse numero
5. 
input numero
for tabuada in range 1,11
print numero * tabuada
'''
numero = int(input('Digite um número: '))
for tabuada in range(1,11):
  print(tabuada, 'X', numero, '=', (tabuada*numero))