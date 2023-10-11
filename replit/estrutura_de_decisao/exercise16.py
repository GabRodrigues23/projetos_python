# Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
# - Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
# - Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
# - Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
# - Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

import math


a = int(input('Digite o valor de a: '))
if a == 0:
  print('Isso não é uma equação!')

else:
  b = int(input('Digite o valor de b: '))
  c = int(input('Digite o valor de c: '))
  
  print('Equaçao do 2° grau da forma: ax² + bx + c')
  
  delta = b*b - (a*4*c)
  if delta < 0:
    print('A equação não possuí raíz!')

  elif delta == 0:
    raiz = -b / (2*a)
    print('A equação possuí apenas uma raiz: {.:f}'.format(raiz))
  
  elif delta > 0:
    raiz1 = (-b - math.sqrt(delta)) / (2*a)
    raiz2 = (-b + math.sqrt(delta)) / (2*a)
    print('A equação possuí duas raizes: ', raiz1, ', ', raiz2)