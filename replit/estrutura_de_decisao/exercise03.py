# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. 

gen = int(input('Digite o número referênte ao seu genero\n 1 - Homem \n 2 - Mulher \n 3 - Outros \n --> '))
if gen == 1:
  print('Você é Homem!')
elif gen == 2:
  print('Você é Mulher')
elif gen == 3:
  print('Você prefere não dizer seu Sexo!')
else:
  print('Error')