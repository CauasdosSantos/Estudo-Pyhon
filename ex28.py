from random import  randint
import time
computador = randint(0,5)
print('-=-'*20)
print('Vou pensar em um nuemro entre 0 e 5. tente adivinhar....')
print('-=-'*20)
jogador = int(input('Em que numero eu pensei? '))
print('PROCESSANDO.......')
time.sleep(3)
if jogador == computador:
    print('parabens vc consegui me vencer!')
else:
    print('Ganhei, seu otario muito ruim lixo aposenta!!!!!! pensei no numero {} seu bosta'.format(computador))

