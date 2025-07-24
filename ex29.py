velocidade = float(input('Digite sua velocidade: '))
if velocidade > 80:
    print('MULTADO! você exedeu o limite permitido que é de 80KM/H')
    multa = (velocidade-80) * 7
    print('Voce deve pagar uma multa de R${:.2f}'.format(multa))
print('Tenah um bom dia! Dirija com segurança')