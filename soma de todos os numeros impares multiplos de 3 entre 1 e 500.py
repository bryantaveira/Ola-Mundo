n = 0
n2 = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        n2 += 1 # mesma coisa que fazer: n2 = n2 +1
        n += c # mesma coisa que fazer: n = n + c
print('A soma de todos os {} numeros impares entre 1 e 500 é {}'. format(n2, n))
