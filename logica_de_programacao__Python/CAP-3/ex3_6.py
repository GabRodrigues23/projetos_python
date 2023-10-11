print('Série de Fibonacci')

ultimo=1
penultimo=1
termo = 1

count=3
while count <= 20:
    print(termo)
    termo = ultimo + penultimo
    penultimo = ultimo
    ultimo = termo
    count += 1
print(termo)