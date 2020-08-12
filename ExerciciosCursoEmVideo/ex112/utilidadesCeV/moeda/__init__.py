def aumentar(preço=0, taxa=0, formato=False):
    res = preço + (preço * (taxa / 100))
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * (taxa / 100))
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda} {preço:.2f}'.replace('.', ',')


def linha():
    print('~' * 35)


def resumo(preço=0, AP=10, DP=5):
    linha()
    print(f'RESUMO DO VALOR'.center(35))
    linha()
    print(f'Preço Analisado: \t{moeda(preço)}.')
    print(f'Dobro de preço: \t{moeda(dobro(preço))}.')
    print(f'Metade do preço: \t{moeda(metade(preço))}.')
    print(f'{AP}% de aumento: \t{moeda(aumentar(preço, AP))}.')
    print(f'{DP}% de redução: \t{moeda(diminuir(preço, DP))}.')
    linha()
