a = float(input('Digite o primeiro valor'))
b = float(input('Digite o segundo valor'))
c: float = float(input('Digite o terceiro valor'))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if a < c and c > b:
    maior = c
print('o menor valor foi {:.1f} e o maior valor foi {:.1f}'.format(menor, maior))
