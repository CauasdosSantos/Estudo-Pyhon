from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é sua jogada? '))
print('-='*15)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('-='*15)
if computador == 0:
    if jogador == 0:
        print('Enpate!!')
    elif jogador == 1:
        print('Jogador ganhou!!')
    elif jogador == 2:
        print('Computador ganhou!!')
elif computador == 1:
    if jogador == 0:
        print('Computador ganhou!!')
    elif jogador == 1:
        print('Enpate!!')
    elif jogador == 2:
        print('Jogador ganhou!!')
elif computador == 2:
    if jogador == 0:
        print('Joagor ganhou!!')
    elif jogador == 1:
        print('Computador ganhou!!')
    elif jogador == 2:
        print('Enpate!!')




