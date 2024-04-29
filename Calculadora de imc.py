n1 = float(input('Digite seu peso:'))
n2 = float(input('Digite sua altura em metros:'))
imc = n1 / (n2 ** 2)
print('seu IMC é de {:.1f}'.format(imc))
if imc < 17:
    print('Cuidado, você esta muito abaixo do peso!!!')

elif imc >= 17 and imc < 18.49:
    print('Você esta abaixo do peso!')

elif imc >= 18.5 and imc < 24.99:
    print('Voce esta no peso normal!')

elif imc >= 25 and imc < 29.99:
    print('Voce esta acima do peso!')

elif imc >= 30 and imc < 34.99:
    print('Cuidade, voce esta com obesidade I!')

elif imc >= 35 and imc < 39.99:
    print('Cuidado, voce esta com obesidade II!')

else:
    print('Voce esta com obesidade III!')
