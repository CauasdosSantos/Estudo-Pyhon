cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)
print('A hipotenusa é {:.3f}'.format(hipotenusa))

'''import math
cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = math.hypot(cateto_adjacente, cateto_oposto)
print('A hipotenusa é {:.3f}'.format(hipotenusa))'''
