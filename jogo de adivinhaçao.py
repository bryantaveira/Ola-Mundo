from random import randint
from time import sleep #adiciona um tempo de espera ao script
cpu = randint(0, 5)
print('-=-' * 10)
print('acerte o numero que eu pensei!')
print('-=-'*10)
player = int(input('em que numero eu pensei?'))
print('Processando...')
sleep(2)
if player == cpu:
    print('Parabens voce me venceu eu pensei no numero {}!!!'.format(cpu))
else:
    print('HAHA eu ganhei ê.3ê eu pensei no numero {} '.format(cpu))