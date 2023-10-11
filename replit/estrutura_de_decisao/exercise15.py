# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

l1 = int(input('Digite o tamanho do 1° Lado: '))
l2 = int(input('Digite o tamanho do 2° Lado: '))
l3 = int(input('Digite o tamanho do 3° Lado: '))

if (l1 + l2 < l3) or (l1 + l3 < l2) or (l2 + l3 < l1):
  print('Isso não é um Triângulo')
elif l1 == l2 and l1 == l3: #todos os lados iguais
  print('Esse é um Triângulo Equilátero!') 
elif (l1 == l2) or (l1 == l3) or (l2 == l3): #dois lados iguais
  print('Esse é um Triângulo Isósceles!')
elif l1 != l2 and l1 != l3: #todos os lados diferentes
  print('Esse é um Triângulo Escaleno!')
