# Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = int(input('Digite o 1° número: '))
n2 = int(input('Digite o 2° número: '))
n3 = int(input('Digite o 3° número: '))
numbers = [n1, n2, n3]
numbers.sort(reverse = True)
print(numbers)