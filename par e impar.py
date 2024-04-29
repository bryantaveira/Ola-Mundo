#cria uma estrutura de repietiçao de 1 até 10
for x in range(1, 10):
   #cria uma variavel numero que recebe um valor do usuario
    numero = float(input('Digite um numero! '))
   # cria uma estrutura de condiçao com a variavel numero
   # e se a diferença da divaçao entre esse numero e 2 é igual a 0
    if numero % 2 == 0:
        print("par")

    else:
        print('impar')
print('fim')
        