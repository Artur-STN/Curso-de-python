from time import sleep
print('\033[31m=\033[m' * 30)
print('{}     10 TERMOS DE UMA PA{}'.format('\033[32m', '\033[m'))
print('\033[31m=\033[m' * 30)
pt = int(input('{}Primeiro Termo: {}'.format('\033[32m', '\033[m')))
r = int(input('{}Razão: {}'.format('\033[33m', '\033[m')))
print('\033[33m=\033[m' * 30)
contador = 1
while contador <= 10:
    print('{}{:2}° Termo: {}{}'.format('\033[34m', contador, pt, '\033[m'))
    sleep(1)
    contador += 1
    pt += r
print('\033[33m=\033[m' * 30)
sleep(1)
print('{}ACABOU{}'.format('\033[36m', '\033[m'))
sleep(1)
