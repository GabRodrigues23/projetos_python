print('\nEquação de 2° grau')

a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))

delta = (b**2) - (4*a*c)
# print(delta)

r1 = (b + (delta ** 0.5)) / 2 * a 
r2 = (b - (delta ** 0.5)) / 2 * a

print('Raízes: ({:.1f} , {:.1f})'.format(r1,r2))