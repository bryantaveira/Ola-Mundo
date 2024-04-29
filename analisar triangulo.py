print("-=-"*25)
print('Analisador de triangulos!')
print('-=-'*20)
a = float(input('Digite a primeira reta! '))
b = float(input('Digite a segunda reta! '))
c = float(input('Digite a terceira reta! '))
if a < b + c and b < c + a and c < b + a:
    print(' suas retas formam um triangulo!')
    if a == b == c:
        print('Equilatero')
    elif a != b != c != a:
        print('escaleno')
    else:
        print('isoceles')
else:
    print('suas retas nao formam um triagulo')