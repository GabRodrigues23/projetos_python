# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# - A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# - A mensagem "Reprovado", se a média for menor do que sete;
# - A mensagem "Aprovado com Distinção", se a média for igual a dez.

'''
1. O usuário deverá informar as notas
2. dadas as notas o programa deverá informar a média
3. valores inteiros ou decimais
4. o programa deverá dizer de acordo com a média se o aluno foi aprovado, reprovado ou reprovado com distinção
5. 
input nota1
input nota2
media = (nota1 + nota2) / 2
if media > 7
  print aprovado
if media < 7
  print reprovado
if media = 7
  print aprovado com distinção
'''

nota1 = float(input('Digite a 1° nota: ').replace(',','.'))
nota2 = float(input('Digite a 2° nota: ').replace(',','.'))
media = (nota1 + nota2) / 2
if media > 7 and media <= 10:
  print('Você foi aprovado!')
elif media < 7 and media >= 0:
  print('Você foi reprovado!')
elif media == 7:
  print('Você foi aprovado com distinção')
else:
  print('Isso não é um valor válido!')
