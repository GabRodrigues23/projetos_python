# Faça um Programa que peça as 4 notas bimestrais e mostre a média. Acrescente dizendo se o aulo passou ou não de acordo com a média

nota1 = int(input('Digite a nota do 1° bimestre: '))
nota2 = int(input('Digite a nota do 2° bimestre: '))
nota3 = int(input('Digite a nota do 3° bimestre: '))
nota4 = int(input('Digite a nota do 4° bimestre: '))

media = (nota1 + nota2 + nota3 + nota4) /4
print('Sua média é:', media)

if media >= 7 and media <= 10:
  print('Parabéns, você passou!')
elif media < 7 and media >= 0:
  print('Você foi Reprovado!')
else:
  print('Valores não conferem, tente novamente')