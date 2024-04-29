from random import randint
import emoji
from time import sleep
tesoura = emoji.emojize(':victory_hand: Tesoura')
papel = emoji.emojize(':raised_hand: Papel')
pedra = emoji.emojize(':raised_fist: Pedra')
cpu = (tesoura, pedra, papel)
random = randint(0, 2)
print('{:=^64}'.format(' VAMOS JOGAR '))
print('\n', end='')
print("_" * 67)
print('''| O jogo é pedra, papel e tesoura, escolha uma opçao para começar:|
| [1] Pedra                                                       |
| [2] Papel                                                       |
| [3] Tesoura                                                     |''')
print('{}'.format('-' * 67))
player = int(input('Digite sua opção: '))
if player == 1:
    cpu = cpu[random]
    if cpu == pedra:
        sleep(1)
        print('JOOO....')
        sleep(1.5)
        print('KEEN....')
        sleep(1.5)
        print('POO....')
        sleep(0.5)
        print('eu escolhi {}, voce escolheu {}, EMPATAMOS!'.format(cpu, pedra))
    elif cpu == papel:
        sleep(1)
        print('JOOO....')
        sleep(1.5)
        print('KEEN....')
        sleep(1.)
        print('POO....')
        sleep(0.5)
        print('eu escolhi {}, voce escolheu {}, VOCE PERDEU!'.format(cpu, pedra))
    else:
        sleep(1)
        print('JOOO....')
        sleep(1.5)
        print('KEEN....')
        sleep(1.5)
        print('POO....')
        sleep(0.5)
        print('eu escolhi {}, voce escolheu {}, VOCE GANHOU!'.format(cpu, pedra))
elif player == 2:
    cpu = cpu[random]
    if cpu == pedra:
        sleep(1)
        print('JOOO....')
        sleep(1.5)
        print('KEEN....')
        sleep(1.5)
        print('POO....')
        sleep(0.5)
        print('eu escolhi {}, voce escolheu {}, VOCE GANHOU!'.format(cpu, papel))
    elif cpu == papel:
        sleep(1)
        print('JOOO....')
        sleep(1.5)
        print('KEEN....')
        sleep(1.5)
        print('POO....')
        sleep(0.5)
        print('eu escolhi {}, voce escolheu {}, EMPATAMOS!'.format(cpu, papel))
    else:
        sleep(1)
        print('JOOO....')
        sleep(1.5)
        print('KEEN....')
        sleep(1.5)
        print('POO....')
        sleep(0.5)
        print('eu escolhi {}, voce escolheu {}, VOCE PERDEU!'.format(cpu, papel))
elif player == 3:
    cpu = cpu[random]
    if cpu == pedra:
        sleep(1)
        print('JOOO....')
        sleep(1.5)
        print('KEEN....')
        sleep(1.5)
        print('POO....')
        sleep(0.5)
        print('eu escolhi {}, voce escolheu {}, VOCE PERDEU!'.format(cpu, tesoura))
    elif cpu == papel:
        sleep(1)
        print('JOOO....')
        sleep(1.5)
        print('KEEN....')
        sleep(1.5)
        print('POO....')
        sleep(0.5)
        print('eu escolhi {}, voce escolheu {}, VOCE GANHOU!'.format(cpu, tesoura))
    else:
        sleep(1)
        print('JOOO....')
        sleep(1.5)
        print('KEEN....')
        sleep(1.5)
        print('POO....')
        sleep(0.5)
        print('eu escolhi {}, voce escolheu {}, EMPATAMOS!'.format(cpu, tesoura))
else:
    print('deu erro')
