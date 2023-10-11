# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

'''
1. O usuário deverá escrever uma letra
2. O programa deverá dizer se essa letra é uma vogal ou consoante
3. deverá ser uma letra
4. O programa deverá dizer se a letra digitada é uma vogal ou consoante
5. 
input letra
if letra a, e, i, o, u
  print vogal
else
  print consoante
'''
letra = input('Digite uma letra: ')
vogal = 'AaEeIiOoUu'
if letra.isalpha():
  if letra in vogal:
    print('A letra {} é uma vogal!'.format(letra))
  else:
    print('A letra {} é uma consoante!'.format(letra))
elif letra.isnumeric():
  print('Você digitou um número!')
else:
  print('Isso não é uma letra!')
