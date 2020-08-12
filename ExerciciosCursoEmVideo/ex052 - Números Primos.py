num = int(input('\033[35mDigite um número: \033[m'))
print('='*20)
cont = 0
for primos in range(1, num+1):
    if num % primos == 0:
        cont += 1
        primos = ('\033[32m{}\033[m'.format(primos))
    else:
        primos = ('\033[31m{}\033[m'.format(primos))
    print(primos, end=' ')
print('\n====================')
print('\n\033[35mO número {} foi dividido {} vezes.\033[m'.format(num, cont))
print('='*20)
if cont <= 2:
    print('\033[32mPortando {} é um número PRIMO.\033[m'.format(num))
else:
    print('\033[31mPortando {} NÂO é um número PRIMO.\033[m'.format(num))
print('='*20)
