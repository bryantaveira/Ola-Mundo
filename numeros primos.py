numero = int(input('digite um número: '))
encremento = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        encremento += 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end=' ')
print('o número {} foi dividido por {} números'.format(numero, encremento))
if numero % c == 0:
        print(f'o número {numero} é primo')
else:
        print(f'o númeor{numero} não é primo')
