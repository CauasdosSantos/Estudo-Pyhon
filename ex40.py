nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segudna nota: '))
media = (nota1 + nota2)/2
print('Sua media foi {}'.format(media))
if media > 7.0:
    print('Aprovado')
elif media >= 5.0 and media <= 6.9:
    print('recuperação')
elif media < 5.0:
    print('Reprovado')
