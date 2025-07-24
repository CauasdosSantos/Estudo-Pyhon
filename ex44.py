print('{:=^40}'.format(' LOJAS CAUAS '))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual opção?  '))
if opção == 1:
    total = preço - (preço * 0.10)
elif opção == 2:
    total = preço - (preço * 0.05)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra sera párcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preço + (preço * 0.20)
    totparc = int(input('Quantas parcela?:'))
    parcela = total / totparc
    print('Sua comrpa sera parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = preço
    print('OPÇÃO INVALIDA DE PAGAEMNTO. tente novamente')
print(('Sua compra de R${:.2f} vai custar R${:.2f} no final').format(preço, total))


