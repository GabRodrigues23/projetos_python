# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:                                               Para homens: (72.7*h) - 58                                      Para mulheres: (62.1*h) - 44.7

altura = float(input('Digite a sua altura: ').replace(',','.'))
h = (72.7 * altura) - 58
m = (62.1 * altura) - 44.7
print('O peso ideal para um Homem de acordo com a sua altura é de: {:.2f}'.format(h))
print('O peso ideal para uma Mulher de acordo com a sua altura é de: {:.2f}'.format(m))