c = 0
n1 = int(input('digite um numero: '))
for n in range(1, 9, 1):
    c += 1
    n = n * n1
    print('{} x {} = {}'.format(c, n1, n))