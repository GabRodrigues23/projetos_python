# Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

periodo = int(input('Digite o período que você estuda: \n[1]-Matutino \n[2]-Vespertino \n[3]-Noturno \n--> '))

if periodo == 1:
  print('Bom Dia!')
elif periodo == 2:
  print('Boa Tarde!')
elif periodo == 3:
  print('Boa Noite!')
else:
  print('Valor Inválido!')