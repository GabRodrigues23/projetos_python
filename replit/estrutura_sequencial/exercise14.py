# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peso_peixe = float(input('Digite o peso total dos peixes pescados: ').replace(',','.'))
if peso_peixe > 50:
  multa = (peso_peixe - 50) * 4
  print('O limite de peso foi excedido, portanto você recebeu uma multa de {:.2f} reais!'.format(multa))
elif peso_peixe <= 50:
  print('Você não levou multa!')