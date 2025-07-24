nun1 = int(input('Digite o primeiro numero: '))
nun2 = int(input('Digite o segundo numero: '))
nun3 = int(input('Digite o terceiro numero: '))
#verificando o menor valor
menor =nun1
if nun2 < nun1 and nun2 < nun3:
    menor = nun2
if nun3 < nun1 and nun3 < nun2:
    menor =nun3
#verificando o maior valor
maior = nun1
if nun2 > nun1 and nun2 > nun3:
    maior = nun2
if nun3 > nun1 and nun3 > nun2:
    maior = nun3
print('0 maior valor foi {}'.format(maior))
print('0 menor valor foi {}'.format(menor))


