frase = str(input('Digite sua frase?: ')).strip()
print('A letra A aparece {}'.format(frase.upper().count('A')))
print('A latre A aparece pela primeira vez na posição {}'.format(frase.upper().find('A')+1 ))
print('A letra A aparece pela ultima vez na posição {}'.format((frase.upper().rfind('A')+1)))