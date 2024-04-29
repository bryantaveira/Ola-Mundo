n1 = int(input('Digite um numero inteiro!'))
print('''Escolha uma das bases para conversao:
[1] Converter para Binario
[2] Converter para Octal
[3] Converter para Hexadecimal''')
n2 = int(input('Qual a sua opção: '))
if n2 == 1:
    print('A conversao de {} para binario fica: {}'.format(n1, bin(n1)[2:]))
elif n2 == 2:
    print('A conversao de {} para octal fica: {}'.format(n1, oct(n1)[2:]))
elif n2 == 3:
    print('A conversao de {} para hexadecimal fica: {}'.format(n1, hex(n1)[2:]))
else:
    print('Opçao invalida tente novamente!')