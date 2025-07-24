from datetime import date
atual = date.today().year
nasc = int(input('ano de nascimento: '))
idade = atual - nasc
print('Sua idade é {}'.format(idade))
if idade <=9:
    print('Atleta MIRIM')
elif idade <= 14:
    print('Atleta infantil')
elif idade <= 19:
    print('Atleta JUNIOR')
elif idade <= 25:
    print('Atleta SÊNIOR')
else:
    print('Atleta MASTER')
