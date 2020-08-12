from random import randint
from time import sleep
lista = list()


def linha():
    print('-' * len('Somando os valores pares de [00, 00, 00, 00, 00]:'))


def sorteia():
    for c in range(5):
        lista.append(randint(1, 10))


def somaPar():
    linha()
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    sleep(0.5)
    print(f'Sorteando {len(lista)} valores: {lista}')
    sleep(0.5)
    print('Pronto!')
    linha()
    sleep(0.5)
    print(f'Somando os valores pares de {lista}:')
    sleep(0.5)
    linha()
    print(f'Resultado: {soma}')
    sleep(0.5)


# Programa Principal
sorteia()
somaPar()
