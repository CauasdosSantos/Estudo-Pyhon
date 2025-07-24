n1 = float(input('Primeiro segmento: '))
n2 = float(input('Primeiro segmento: '))
n3 = float(input('Primeiro segmento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n2 + n1:
    print('OS segmentos podem formar um triangulo!', end='')
    if n1 == n2 == n3:
        print('Triangulo equilatero!')
    elif n1 != n2 != n3 != n1:
        print('Triangulo escaleno!')
    else:
        print('Triangulo isosceles')
else:
    print('Os segmentos não pdoem se formar um triangulo')