from math import pi

print('\nCalcular o raio de uma esfera!')

r = int(input("Digite o valor do raio: "))
vol = (4 / 3) * pi * r**3

print(f'O volume da esfera é: {vol:.2f}')