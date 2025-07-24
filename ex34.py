salario = float(input('Digite seu salario? R$'))
if salario <= 1250:
    aumento = salario * 0.15
    novo_salario = salario + aumento
else:
    aumento = salario * 0.10
    novo_salario = salario + aumento
print('O seu salario de R${} aumentou para R${}'.format(salario, novo_salario))