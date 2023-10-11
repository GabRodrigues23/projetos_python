# Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

dia = int(input(' 1 - Domingo\n 2 - Segunda-Feira\n 3 - Terça-Feira\n 4 - Quarta-Feira\n 5 - Quinta-Feira\n 6 - Sexta-Feira\n 7 - Sábado\nDigite o número equivalente ao dia Desejado: '))
if dia == 1:
  print('Você escolheu Domingo!')
elif dia == 2:
  print('Você escolheu Segunda-Feira!')
elif dia == 3:
  print('Você escolheu Terça-Feira!')
elif dia == 4:
  print('Você escolheu Quarta-Feira!')
elif dia == 5:
  print('Você escolheu Quinta-Feira!')
elif dia == 6:
  print('Você escolheu Sexta-Feira!')
elif dia == 7:
  print('Você escolheu Sábado!')
else:
  print('Digito Inválido')