# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.                       f = ((c * 9) / 5) + 32 ou (c * 1,8) + 32

c = float(input('Digite a temperatura em Graus Celsius: ').replace(',','.'))
f = ((c * 9) / 5) + 32
print('A temperatura em Graus Fahrenheit é de: {:.1f}°F'.format(f))