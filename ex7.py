nota1 = float(input('digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))
media = (nota1 + nota2)/2
print('a media do aluno é {}'.format(media))
if media >= 6.0:
    print('aprovado')
else:
    print('reprovado')