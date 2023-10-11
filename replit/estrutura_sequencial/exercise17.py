# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros;
# comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''
1. tamanho da área a ser pintada
2. informar quantas tintas deverão ser compradas, considerando latas de 3,6L e 18L
3. 
4. Informar a quantidade de tintas a serem compradas e o valor total a ser gasto
5.
input = area
if 
  print(deverao ser compradas ... latas de 18l, valor)
elif
  print(deverao ser compradas ... latas de 3,6l, valor)
elif
  desc = valor * 0.10
  valor = valor - desc
  print(deverao ser compradas ... latas de 18l e ... latas de 3,6l, valor)
------------------------------
1l -> 6m
lata18 = 80 reais
lata3 = 25 reais
'''

area = int(input('Digite a área a ser pintada: '))
metro_litro = 18 / 6
litro_tinta = area / 6