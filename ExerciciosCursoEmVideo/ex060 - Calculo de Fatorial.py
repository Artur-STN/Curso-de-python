from math import factorial
print('\033[36;1m▼▲\033[m'*25)
num = int(input('{}Digite um número para calcular o seu Fatorial:{} '.format('\033[31;1m', '\033[m')))
print('\033[36;1m▼▲\033[m'*25)
c = num
print('''{}Calculando...{}
{}{}! ='''.format('\033[31;1m', '\033[m', '\033[33;1m', num), end=' ')

while c > 0:

    if c == 1:
        print(' {} = {}'.format(c, factorial(num)), end='')
    elif c != 1:
        print('{} x '.format(c), end='')
    c -= 1
print('\n')
print('O fatorial de {} é {}'.format(num, factorial(num)))
print('\033[36;1m▼▲\033[m'*25)
