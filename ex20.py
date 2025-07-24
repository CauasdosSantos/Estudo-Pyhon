import random
n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('terceiro aluno: ')
n4 = input('Quarto aluno: ')
lista_apresentação = [n1, n2, n3, n4]
random.shuffle(lista_apresentação)
print('A ordem de apresentaçã sera')
print(lista_apresentação)