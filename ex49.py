nun = int(input('Digite um nuemro para ver sua tabuada: '))
print('-='*6)
for c in range(1, 11):
    print('{} x {:2} = {}'.format(nun, c, nun * c))
print('-='*6)