from datetime import date
genero = str(input('Voce é homem ou mulher: ')).upper()
atual = date.today().year
nasc = int(input('Ano de nasciemnto: '))
idade = atual - nasc
if genero in 'HOMEM' and idade < 18 and idade < 18 and idade > 18:
    print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
    print('Voce é homem')
    print('Voce deve se alistar imediatamente!')
    saldo = 18 - idade
    print('Voce ainda não tem 18 anos. ainda falntem {} anos para o alsitamento'.format(saldo))
    ano = atual + saldo
    print('Faltam tanos {} anos para seu alsitamento'.format(ano))
    saldo = idade - 18
    print('Voce ja deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('seu alistamebnto foi em {} '.format(ano))
elif genero == 'MULHER':
    print('Voce esta dispensado do serviço militar')
