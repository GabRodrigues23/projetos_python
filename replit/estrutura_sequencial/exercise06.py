# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = float(input('Digite o valor do Raio: ').replace(',','.'))
area = 3.14 * (raio * 2)
diametro = raio * 2
print('O valor do Diâmetro do Círculo é de: {:.1f}'.format(diametro))
print('O valor da Área do Círculo é de: {:.1f}'.format(area))