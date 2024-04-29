from datetime import date
nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print('Sua idade é de {} anos'.format(idade))
if idade < 9:
    print('Categoria mirim')
elif idade >= 9 and idade <= 14:
    print('Categoria infantil')
elif idade > 14 and idade <= 19:
    print('Categoria junior')
elif idade > 19 and idade <= 25:
    print('Categoria Senior')
else:
    print('Categoria master')