print('\nClassificação de idade!')

idade = int(input('Digite sua idade: '))

if(idade < 5):
    print('Você ainda é muito novo para se candidatar')
elif(idade >= 5 and idade <= 7):
    print('Infantil A')
elif(idade >= 8 and idade <= 10):
    print('Infantil B')
elif(idade >= 11 and idade <= 13):
    print('Juvenil A')
elif(idade >= 14 and idade <= 17):
    print('Juvenil B')
else:
    print('Adulto')