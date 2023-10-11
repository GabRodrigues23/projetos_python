# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 25%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 20%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 15%
# salários de R$ 1500,00 em diante : aumento de 10% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento

salario = float(input('Digite seu salário atual: ').replace(',','.'))

reajuste = salario * 0.25


if salario < 280:
  
  novo_salario = salario + reajuste

  print('Seu salario terá um aumento de 25%, equivalente à R${:.2f}'.format(reajuste))
  print('Seu novo salário é de R${:.2f}'.format(novo_salario))


elif salario >= 280 and salario < 700:
  
  reajuste = salario * 0.20
  novo_salario = (salario + reajuste)

  print('Seu salario terá um aumento de 20%, equivalente à R${:.2f}'.format(reajuste))
  print('Seu novo salário é de R${:.2f}'.format(novo_salario))


elif salario >= 700 and salario < 1500:

  reajuste = salario * 0.15
  novo_salario = salario + reajuste
  
  print('Seu salario terá um aumento de 15%, equivalente à R${:.2f}'.format(reajuste))
  print('Seu novo salário é de R${:.2f}'.format(novo_salario))


elif salario >= 1500:

  reajuste = salario * 0.10
  novo_salario = salario + reajuste
  
  print('Seu salario terá um aumento de 10%, equivalente à R${:.2f}'.format(reajuste))
  print('Seu novo salário é de R${:.2f}'.format(novo_salario))