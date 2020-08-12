from random import randint
from time import sleep


def sorteio():
    print('sorteando exercício para revisão..')
    sleep(1.5)
    print('exercício sorteado, o exercício que você deverá revisar é o exercício', randint(1, 115 + 1))


while True:
    try:
        sortear = str(input('deseja sortear um exercício? ')).strip().lower().split()
    except:
        print('digite apenas sim ou não.')
    else:
        if 'sim' in sortear:
            sorteio()
        elif 'nao' in sortear or 'não' in sortear:
            break
        else:
            print('digite apenas sim ou não.')
        while True:
            try:
                again = str(input('\nsortear outro? ')).strip().split()
            except:
                print('responda apenas com sim/não.')
                continue
            else:
                if 'sim' in again:
                    sorteio()
                    continue
                elif 'não' in again or 'nao' in again:
                    print('muito bem, vá revisar então..')
                    sleep(1)
                    break
        break
