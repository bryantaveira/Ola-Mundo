print('{:=^40}'.format(' LOJA DO BRYAN '), '\n')
print('-' * 37, '''\nEscolha uma das formas de pagamento:
[1] Á vista / Cheque (desconte de 10%):
[2] Á vista no cartão (desconto de 5%):
[3] Até 2x no cartão (sem juros):
[4] Em 3x ou mais no cartão (juros de 20% ao mes) :''')
print('-' * 37)
valor = float(input('Digite o valor do produto: '))
opçao = int(input('Digite a forma de pagamento: '))
if opçao == 1:
    desconto = valor * 10 / 100
    total = valor - desconto
    print('Desconto de 10%, o valor total da compra R${}!'.format(total))
elif opçao == 2:
    desconto = valor * 5 / 100
    total = valor - desconto
    print('Desconto de 5%, o valor total da compra R${}!'.format(total))
elif opçao == 3:
    total = valor / 2
    print('Parcelado em 2x, cada parcela será de R${}, o valor total da compra R${}!'.format(total, valor))
elif opçao == 4:
    vezes = int(input('Quantas vezes: '))
    if vezes < 3:
        print('Quantidade de parcelas insuficientes, por favor tente novamente!')
    else:
        juros = ((valor * 2) / 100) * 12
        parcela = (valor + juros) / vezes
        total = valor + juros
        print('Parcelado em {}x, cada parcela será de R${}, o valor total da compra R${}!'.format(vezes, parcela, total))
else:
    print('Opção invalida, tente novamente!')
4