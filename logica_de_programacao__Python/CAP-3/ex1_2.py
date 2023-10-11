print('\nDistância entre pontos do plano P e Q!')

x1 = int(input('Ponto x do 1° plano: '))
y1 = int(input('Ponto y do 1° plano: '))

x2 = int(input('Ponto x do 2° plano: '))
y2 = int(input('Ponto y do 2° plano: '))

d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print(f'A distância entre os pontos é: {d:.2f}!')