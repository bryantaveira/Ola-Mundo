mm,cm, dm, m, km = 0, 0, 0, 0, 0,

v = "sim"
print('{:=^50}'.format(' CONVERSOR DE MEDIDAS '))
print('''Escolha uma das opçoes a seguir:
[MM] para milimetros
[DM] para decimetros
[CM] para centimetros
[M] para metros
[KM] para quilometros''')
while v not in 'nao':
    m1 = input('Digite qual medida a ser convertida: ').upper()
    m2 = int(input('Qual o tamanho da medida: '))
    m3 = input('Digite para qual medida voce que converter: ').upper()
    if m1 == 'MM':
        if m3 == 'CM':
            cm = m2 / 10  # centimetros
            print('cm {}'.format(cm))
        elif m3 == 'DM':
            dm = m2 / 100  # decimetro
            print('dm {}'.format(dm))
        elif m3 == 'M':
            m = m2 / 1000  # metros
            print('m {}'.format(m))
        elif m3 == 'KM':
            km = m2 / 1000000 # km
            print('km {}'.format(km))
        else:
            print('Não cadastrado')
    #############################################################
    elif m1 == 'CM':
        if m3 == 'MM':
            mm = m2 * 10  # milimetros
            print('mm {}'.format(mm))
        elif m3 == 'DM':
            dm = m2 / 100  # decimetro
            print('dm {}'.format(dm))
        elif m3 == 'M':
            m = m2 / 1000  # metros
            print('m {}'.format(m))
        elif m3 == 'KM':
            km = m2 / 1000000 # km
            print('km {}'.format(km))
        else:
            print('Não cadastrado')
    ############################################################
    elif m1 == 'DM':
        if m3 == 'MM':
            mm = m2 * 100  # milimetros
            print('mm {}'.format(mm))
        elif m3 == 'CM':
            cm = m2 * 10  # centimetro
            print('cm {}'.format(cm))
        elif m3 == 'M':
            m = m2 / 10  # metros
            print('m {}'.format(m))
        elif m3 == 'KM':
            km = m2 / 10000 # km
            print('km {}'.format(km))
        else:
            print('Não cadastrado')
    ##########################################################
    elif m1 == 'M':
        if m3 == 'MM':
            mm = m2 * 1000  # milimetros
            print('mm {}'.format(mm))
        elif m3 == 'DM':
            dm = m2 * 10  # decimetro
            print('dm {}'.format(dm))
        elif m3 == 'CM':
            cm = m2 * 100  # metros
            print('cm {}'.format(cm))
        elif m3 == 'KM':
            km = m2 / 1000 # km
            print('km {}'.format(km))
        else:
            print('Não cadastrado')
    ##########################################################
    elif m1 == 'KM':
        if m3 == 'MM':
            mm = m2 * 1000000  # milimetros
            print('mm {}'.format(mm))
        elif m3 == 'DM':
            dm = m2 * 10000  # decimetro
            print('dm {}'.format(dm))
        elif m3 == 'M':
            m = m2 * 1000  # metros
            print('m {}'.format(m))
        elif m3 == 'CM':
            cm = m2 * 100000 # km
            print('cm {}'.format(cm))
        else:
            print('Não cadastrado')
    else:
        print('Conversão não cadastrada, tente novamente')
    v = input('voce gostaria de fazer novamente? ')
