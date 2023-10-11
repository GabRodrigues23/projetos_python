# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

usuario = str(input("Usuário: "))
senha = str(input("Senha: "))
print('-------------------------------------')

while usuario == senha:
  print("\nUsuário e Senha não podem ser iguais")
  usuario = str(input("Usuário: "))
  senha = str(input("Senha: "))
  print('-------------------------------------')

else:
  print("\nCadastro realizado com sucesso!")