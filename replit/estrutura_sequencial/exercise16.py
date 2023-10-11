# Faça um programa para uma loja de tintas. O programa deverá pedir o area em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

area = float(input("Área a ser pintada: "))
litro = area / 3

if area % 54 == 0:
  lata = area / 54
elif (area % 54) > 0:
  lata = int(area / 54) + 1 # tag "int" is necessary to the program don't read as decimal and return error
preco = lata * 80
print(f"Latas: {lata:.0f}")
print(f"Preço: R${preco:.2f}")