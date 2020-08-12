def metade(preço=0):
    res = preço / 2
    return res


def dobro(preço=0):
    res = preço * 2
    return res


def aumentar(preço=0, taxa=0):
    taxa = preço + (preço * (10 / 100))
    return taxa


def diminuir(preço=0, taxa=0):
    taxa = preço * (10 / 100)
    return taxa


def linha():
    print('~' * 60)


def moeda(preço=0, moeda='R$'):
    return f'{moeda} {preço:.2f}'.replace('.', ',')
