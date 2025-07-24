massa = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual a sua alatura? (m) '))
imc = massa / (altura ** 2)
print('O IMC dessa pessoa é de {:.2f}'.format(imc))
if imc <= 18.5:
    print('Abaixo do pesso'.format(imc))
elif 18.5 <= imc <= 25:
    print('Peso ideal'.format(imc))
elif 25 <= imc <= 30:
    print('Sobrepeso'.format(imc))
elif 30 <= imc <= 40:
    print('Obsidade'.format(imc))
else:
    print('Obsidade morbida'.format(imc))