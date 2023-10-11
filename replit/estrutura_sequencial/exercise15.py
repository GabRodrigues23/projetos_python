# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

horas_trabalhadas = float(input('Digite o total de horas trabalhadas no dia: ').replace(',','.'))
valor_hora = float(input('Digite o valor recebido por hora trabalhada no dia: ').replace(',','.'))

total = horas_trabalhadas * valor_hora
bruto = (total * 5) * 4
print('Salário Bruto: R${:.2f}'.format(bruto))

ir = bruto * (11 / 100)
inss = bruto * (15 / 100)
sindicato = bruto * (5 / 100)
liquido = ((bruto - ir) - inss) - sindicato

print('IR: R${:.2f}'.format(ir))
print('INSS: R${:.2f}'.format(inss))
print('Sindicato: R${:.2f}'.format(sindicato))
print('Salário Liquido: R${:.2f}'.format(liquido))