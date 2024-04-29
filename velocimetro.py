v = float(input('qual a velocidade do carro? '))
m = (v - 80)*7

if v <= 80:
    print('tenha uma boa viajem')
else:
    print('voce foi multado em {} reais'.format(m))