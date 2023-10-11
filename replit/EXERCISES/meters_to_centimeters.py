# Faça um programa em linguagem Python que converta metros para centímetros.

'''
1. valor em metros
2. transformar o valor em metros em centimetros
3. valor pode ser fraccionario ou não
4. o sistema deverá imprimir o valor em centimetros
5. 
input valor_metro
valor_centimetro = valor_metro / 100
print valor_centimetro *.%1
'''
valor_metro = float(input('Digite o valor em metros: ').replace(',','.'))
valor_centimetro = valor_metro*100
print(valor_centimetro, 'cm')