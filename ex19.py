import random
aluno1 = str(input('Digite o nome do primeiro aluno: '))
aluno2 = str(input('Digite o nome do segundo aluno: '))
aluno3 = str(input('Digite o nome do terceiro aluno: '))
aluno4 = str(input('Digite o nome do quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
aluno_sorteado = random.choice(lista)
if aluno_sorteado  and lista[::]:
    print('O aluno sorteado foi {}'.format(aluno_sorteado))
    print('O aluno é gay',end=' , ')
    print('Os outros alunos não são gays',end='')

