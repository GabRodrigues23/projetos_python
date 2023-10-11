# Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = -1

while nota < 0 or nota > 10:
  nota = int(input("Informe a nota: "))
  if nota >= 0 and nota <= 10:
    print("nota: {:.0f}".format(nota))
  else:
    print("Valor inválido")