from time import sleep


def linha():
    print('-' * 30)


def maior(*núm):
    cont = maior = 0
    print('Analisando os valores passados...')
    for v in núm:
        print(f'{v} ', end='')
        sleep(0.4)
        if cont == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        cont += 1
    print()
    print(f'Foram imformados {cont} valores ao todo.')
    print(f'O Maior valor é {maior}')
    linha()


# programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
