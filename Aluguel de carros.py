n1 = int(input('Quantos dias voce alugou o carro? '))
n2 = float(input('Quantos Km voce andou com o carro? '))
n3 = n1*60+n2*0.15
print('O valor que voce deve pagar é {:.2f}!'.format(n3))