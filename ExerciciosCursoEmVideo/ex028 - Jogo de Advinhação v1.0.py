from random import randint
from time import sleep
na = randint(0, 5)
print('-=-'*20)
print('Vou pensar em um número de 0 a 5. Tente advinhar...')
print('-=-'*20)
num = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(1)
if na == num:
    print('PARABENS!\nVOCÊ GANHOU!')
else:
    print('Eu pensei no número {}.\nVocê perdeu!'.format(na))
print('-=-'*20)
