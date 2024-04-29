import datetime
n1 = int(input('Digite em que ano voce nasceu: '))
n2 = datetime.date.today().year #outra forma de invocar essa classe do modulo é ##from datetime import date## o comando fica mais simples ##date.today().year##
n3 = n2 - n1
print('Voce tem {} anos'.format(n3))
if n3 == 18:
    print(' voce deve se alistar imediatamente!')
elif n3 < 18:
    n3 = 18 - n3
    n4 = n2 + n3
    print('Voce deve se alistar no ano de {} daqui a {} anos'.format(n4, n3))
else:
    n3 = n1 + 18
    n4 = n2 - n3
    print('Voce devia ter se alistado no ano de {} ha {} anos'.format(n3, n4))
