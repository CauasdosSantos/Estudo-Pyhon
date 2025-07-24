num = int(input('Digite um numeor inteiro: '))
print('''Escolha um das bases para conversão: 
[ 1 ] converter para BIANRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL ''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINARIO é igual a {} '.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {} '.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {} '.format(num, hex(num)[2:]))
else:
    print('opção invalida. tente novamente')
