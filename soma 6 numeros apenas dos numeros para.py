acum = 0
cont = 0
for c in range(1, 7):
    n1 = int(input('Digite o valor {}°: '.format(c)))
    if n1 % 2 == 0:
        cont += 1
        acum += n1
print('voce informou {} numeros pares e a soma deles é {}'.format(cont, acum))
