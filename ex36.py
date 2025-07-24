casa = float(input('Qual o valor da casa que deseja comprar? R$ '))
salario = float(input('Informe o seu salario R$ '))
ano = int(input('Em quantos anos voce deseja pagar a casa?: '))
prestação = casa/(ano * 12)
emprestimo = salario * 0.30
print('Para pagar um casa de R${:.2f} em {} anos'.format(casa, ano),end='')
print('a prestação sera  de R${:.2f}'.format(prestação))
if prestação <= emprestimo:
    print('Emprestimo aprovado')
else:
    print('Emprestimo negado')