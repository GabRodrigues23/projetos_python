# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

n1 = float(input('Digite a nota do 1° bim: ').replace(',','.'))
n2 = float(input('Digite a nota do 2° bim: ').replace(',','.'))
if n1 <= 10 and n2 <= 10:
    media = (n1 + n2) /2
    if media >= 7 and media <= 10:
      print('Sua média foi: {:.1f}! Parabéns, você foi aprovado!'.format(media))
    elif media < 7 and media >= 0:
      print('Sua média foi: {:.1f}! Você foi reprovado :('.format(media))
    else:
      print('Error')              
else:
  print('Por favor, digite um número entre 0 e 10!')
