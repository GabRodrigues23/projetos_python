# Fazer um algoritmo que ao receber o salário atual de um funcionário, calcule o valor do novo salário reajustado de acordo com a tabela abaixo: 
# Salário atual	Reajuste
# Abaixo de R$500,00	20%
# de R$500,00 até R$1000,00	15%
# Acima de R$1000,00	10%

'''
1. valor salario do usuario
2. devera calcular de acordo com a tabela e reajustar o valor
3. -
4. o sistema devera imprimir o salario com reajuste
5.
input valor salario
if valor salario < 500
  novo salario = valor salario * 15%
  print novo salario
if valor salario >= 500 and <= 1000
  novo salario = valor salario * 10%
  print novo salario
if valor salario > 1000
  novo salario = valor salario * 5%
  print novo salario
'''

salario = float(input('Digite o valor do seu salário: ').replace(',','.'))
if salario < 500:
  novo_salario = salario + (salario*0.15)
  print('O valor reajustado do seu salário é de:', novo_salario)
elif salario >= 500 and salario <= 1000:
  novo_salario = salario + (salario*0.10)
  print('O valor reajustado do seu salário é de:', novo_salario)
else:
  novo_salario = salario + (salario*0.05)
  print('O valor reajustado do seu salário é de:', novo_salario)
  