from time import sleep
# uad = um até dez
num = int(input('{}Digite um número para ver a sua tabuada: {}'.format('\033[32m', '\033[m')))
uad = 1
print('\033[31m=\033[m'*20)
for tabuada in range(0, 10):
    res = num * uad
    print('{}{}  X {:2} = {}{}'.format('\033[32m', num, uad, res, '\033[m'))
    sleep(1)
    uad += 1
print('\033[31m=\033[m'*20)
