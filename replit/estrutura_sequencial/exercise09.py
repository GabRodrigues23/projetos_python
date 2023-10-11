# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.             c = ((f - 32) / 9) * 5 ou (f - 32) / 1,8

f = float(input('Digite a temperatura em Graus Fahreinheit: ').replace(',','.'))
c = ((f - 32) / 9) * 5
print('A temperatura em Graus Celsius é de: {:.1f}°C'.format(c))