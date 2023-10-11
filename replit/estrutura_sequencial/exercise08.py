# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

horas_trabalhadas = float(input('Digite o total de horas trabalhadas mês: ').replace(',','.'))
valor_hora = float(input('Digite o valor recebido por hora trabalhada no dia: ').replace(',','.'))

total = horas_trabalhadas * valor_hora
total_mensal = (total * 5) * 4

print('Você ganha R${:.2f} por dia'.format(total))
print('Que da um total de R${:.2f} por mês'.format(total_mensal))