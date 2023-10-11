# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

largura = float(input('Digite a Largura: ').replace(',','.'))
altura = float(input('Digite a Altura: ').replace(',','.'))
if altura == largura:
  area = altura * largura
  print('A Area do Quadrado é: {:.1f}'.format(area))
else:
  area = altura * largura
  print('A Area do Retângulo é: {:.1f}'.format(area))