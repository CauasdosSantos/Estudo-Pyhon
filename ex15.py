dia = int(input('quantos dias deseja alugar o carro: '))
Km = float(input('quantidade de KM rodados: '))
pagar = ((dia * 60) + (Km * 0.15))
print('O preço a se pagar pelo caro é {:.2f}'.format(pagar))