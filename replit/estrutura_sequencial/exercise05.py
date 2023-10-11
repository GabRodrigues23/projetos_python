# Faça um Programa que converta metros para centímetros.

valor_m = float(input('Digite um valor em metros: ').replace(',','.'))
valor_cm = valor_m * 100
print('O valor de {}m convertido em cm é de'.format(valor_m), '{}cm'.format(valor_cm))