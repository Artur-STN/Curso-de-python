from random import randint
print('\033[33;1m▼▲\033[m'*10)
num = int(input('\033[34;1mDigite um número:\033[m '))
jogador = str(input('\033[34;1mPar ou Ímpar? [P/I]\033[m ')).upper().strip()[0]
print('\033[33;1m▼▲\033[m'*10)
pc = randint(0, 10)
soma = (num + pc)
pi = ''
if soma % 2 == 0:
    pi = 'P'
else:
    pi = 'I'
total = 0
while True:
    total += 1
    print(f'\033[34;1mVocê jogou {num} e o Computador Jogou {pc}.\033[m')
    if jogador == 'P':
        print('\033[34;1mVocê jogou PAR.\033[m')
    elif jogador == 'I':
        print('\033[34;1mVocê jogou ÍMPAR.\033[m')
    if pi == jogador:
        if pi == 'P':
            print(f'\033[34;1mA soma entre {num} + {pc}  é {soma} deu PAR.\033[m')
        elif pi == 'I':
            print(f'\033[34;1mA soma entre {num} + {pc}  é {soma} deu ÍMPAR.\033[m')
        print('\033[30;1m▼▲\033[m' * 10)
        print('\033[32;1mVOCÊ VENCEU!!!\033[m')
        print('\033[30;1m▼▲\033[m' * 10)
        print('\033[30;1m▼▲\033[m' * 10)
        num = int(input('\033[34;1mDigite um número:\033[m '))
        jogador = str(input('\033[34;1mPar ou Ímpar? [P/I]\033[m ')).upper().strip()[0]
        print('\033[33;1m▼▲\033[m' * 10)
        pc = randint(0, 10)
        soma = (num + pc)
        pi = ''
        if soma % 2 == 0:
            pi = 'P'
        else:
            pi = 'I'
    elif pi != jogador:
        if pi == 'P':
            print(f'\033[34;1mA soma entre {num} + {pc}  é {soma} deu PAR.\033[m')

        elif pi == 'I':
            print(f'\033[34;1mA soma entre {num} + {pc}  é {soma} deu ÍMPAR.\033[m')
        print('\033[31;1m▼▲\033[m' * 10)
        print('\033[31;1mVOCÊ PERDEU!!!\033[m')
        print('\033[31;1m▼▲\033[m' * 10)
        if total == 1:
            total = 0
            print(f'\033[32;1mVocê teve um total de {total} vitórias.\033[m')
            print('\033[33;1m▼▲\033[m' * 10)
        else:
            total -= 1
            print(f'\033[32;1mVocê teve um total de {total} vitórias.\033[m')
            print('\033[33;1m▼▲\033[m' * 10)
        break
