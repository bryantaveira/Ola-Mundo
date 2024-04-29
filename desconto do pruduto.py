n1 = float(input('Digite o valor do produto! '))
n2 = int(input('Digite a porcentagem do desconto! '))
q = (n2/100)*n1
v = n1-q
print('Desconto de {:.2f}, porcentagem do desconto {}% e valor final do produto {:.2f}!'. format(q, n2, v))