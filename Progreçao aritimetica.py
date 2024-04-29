#cria variaveis que receberão os valores do usuario e o calculo da operação
termo = int(input('primeiro termo: '))
razao = int(input('Razão: '))
vezes = int(input('quantas vezes?'))
decimo = (termo + vezes) * razao

#para percorrer um numero na quantidade de vezes escolhida no passo da razão e mostra no terminal
for c in range(termo, decimo, razao):
    print('{}  '.format(c), end='')