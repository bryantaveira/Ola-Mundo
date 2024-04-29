d = float(input('Qual a distancia da  viagem? '))
print('Voce vai fazer uma viagem de {} Km.'.format(d))
if d <= 200:
    v = d * 0.45
else:
    v = d * 0.50
print('sua viagem vai custar {} '.format(v))
