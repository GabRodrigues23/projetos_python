print('\nDecrescente')

num1 = int(input('Digite o 1° número: '))
num2 = int(input('Digite o 2° número: '))
num3 = int(input('Digite o 3° número: '))

if (num1 == num2) or (num2 == num3) or (num1 == num3):
    print('\nNúmeros Iguais')
else:
    #num1 maior
    if (num1 > num2) and (num1 > num3):
        if (num2 > num3): #num1 > num2 > num3
            print("\n{0}, {1}, {2}".format(num1,num2,num3))
        else: #num1 > num3 > num2
            print("\n{0}, {2}, {1}".format(num1,num2,num3))
    #num2 maior
    elif (num2 > num1) and (num2 > num3):
        if (num1 > num3): #num2 > num1 > num3
            print("\n{1}, {0}, {2}".format(num1,num2,num3))
        else: #num2 > num3 > num1
            print("\n{1}, {2}, {0}".format(num1,num2,num3))
    #num3 maior
    else:
        if (num1 > num2): #num3 > num1 > num2
            print("\n{2}, {0}, {1}".format(num1,num2,num3))
        else: #num3 > num2 > num1
            print("\n{2}, {1}, {0}".format(num1,num2,num3))

print("\nFim do Programa!")