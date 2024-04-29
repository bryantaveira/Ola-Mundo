n1 = float(input(' Digite a primeira nota! '))
n2 = float(input(' Digite a segunda nota! '))
m = (n1+n2)/2
if m >= 7:
    print('a media deste aluno é: {:.1f}, aprovado!'.format(m))
elif m < 6:
    print('a media deste aluno é: {:.1f}, reprovado!'.format(m))
else:
    print('a media deste aluno é: {:.1f}, recuperaçao'.format(m))
