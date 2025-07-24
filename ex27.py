nome = str(input('Digite seu nome completo: ')).strip()
nome_separado = nome.split()
print('Seu primeiro mome é {}'.format(nome_separado[0]))
print('Seu ultimo nome é {}'.format(nome_separado[len(nome_separado)-1]))