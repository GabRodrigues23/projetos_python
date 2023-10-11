print('\n--Calculadora--\n')

n1 = int(input("   "))
op = (input(" "))
n2 = int(input("   "))
print("________\n")

if(op == "+"):
    res = n1 + n2
    print(f"   {res}")
elif(op == "-"):
    res = n1 - n2
    print(f"   {res}")
elif(op == "*"):
    res = n1 * n2
    print(f"   {res}")
elif(op == "/"):
    res = n1 / n2
    print(f"   {res}")
else:
    print("Operador Inválido")
print("\n")