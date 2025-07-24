preço = float(input('digite o preço R$ '))
novo_preço = preço * 0.05
preço_descontado = preço - novo_preço
print('O preço do produto com desconmto é {:2f}'.format(preço_descontado))