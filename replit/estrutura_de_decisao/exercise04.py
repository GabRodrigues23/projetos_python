# Faça um Programa que verifique se uma letra digitada é vogal ou consoante. 


letra = input('Digite uma letra \n -> ')
vogal = 'AaEeIiOoUu'

if letra.isalpha():
  if letra in vogal:
    print('Essa letra é uma vogal!')
  else:
    print('Essa letra é uma consoante!')
elif letra.isnumeric():
  print('Isso é um número!')
else:
  print('Caractére Inválido!')