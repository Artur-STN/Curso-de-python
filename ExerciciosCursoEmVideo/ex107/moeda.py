def metade(n=0):
    res = n/2
    return res


def dobro(n=0):
    res = n*2
    return res


def aumentar(n=0, taxa=0):
    taxa = n + (n * (10/100))
    return taxa


def diminuir(n=0, taxa=0):
    taxa = n * (10 / 100)
    return taxa


def linha():
    print('~' * 60)
