casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salario: '))
anos = int(input('Quantas anos de financiamento: '))
prestaçao = casa / (anos * 12)
limite = salario * 30 / 100 #limite de 30% do salario
print(' prestaçao sera de {:.2f}'.format(prestaçao ))
print('o limite é de {}'.format(limite))
if prestaçao <= limite:
    print('concedido')
else:
    print('negado')
