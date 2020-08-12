from random import randint
n = 1
par = impar = 0

while n != 0:
    if n != 0:
        n = randint(0, 10)
        print(n, end=' ')
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print('\nVocê digitou {} números pares.'.format(par))
print('Você digitou {} números ímpares.'.format(impar))
