import random
from time import sleep
itens = ['PEDRA', 'PAPEL', 'TESOURA']
pc = random.randint(0, 2)
print('\033[31m-=-\033[m'*10)
print('''{}SUAS OPÇÕES:{}
{}[ 0 ] PEDRA{}
{}[ 1 ] PAPEL{}
{}[ 2 ] TESOURA{}
'''.format('\033[32m', '\033[m', '\033[33m', '\033[m', '\033[34m', '\033[m', '\033[35m', '\033[m'))
print('\033[31m-=-\033[m'*10)
jogador = int(input('{}Qual é a sua jogada?{} '.format('\033[32m', '\033[m')))
print('\033[31m-=-\033[m'*10)
print('{}Computador jogou {}{}'.format('\033[32m', itens[pc], '\033[m'))
print('{}Jogador jogou {}{}'.format('\033[31m', itens[jogador], '\033[m'))
print('\033[31m-=-\033[m'*10)
if pc == jogador:
    print('\033[31mEMPATE !\033[m')
elif pc != jogador:
    if pc > jogador:
        print('\033[32mComputador Ganhou !')
    elif pc < jogador:
        print('\033[31mJogador Ganhou !')