def fatorial(num=1, show=0):
    """
    ---> Calcula o fatorial de um número.
    :param num: Número escolhido.
    :param show: Retorna se quer ver calculo da fatorial.
    :return: O Fatorial da variavel núm.
    """
    res = 1
    letra = ' X '
    if not show:
        for c in range(1, num+1):
            res *= c
    elif show:
        print(f'{num}! = ', end='')
        for c in range(num, 0, -1):
            if c == 1:
                letra = ' = '
            print(f'{c}', end=letra)
            res *= c
    print(res)


# Programa Principal
help(fatorial)
n = int(input('Quer ver fatorial de qual número? '))
calculo = str(input('Quer ver o calculo? [S/N] ')).upper().strip()[0]
while calculo not in 'SN':
    calculo = str(input('Resposta Ínvalida.'
                        '\nDigite "S" para Sim ou "N" para Não.\nQuer ver o calculo? [S/N] ')).upper().strip()[0]
if calculo == 'S':
    verdOuFalso = True
elif calculo == 'N':
    calculo = False
print('-' * 30)
print('Resultado: ')
fatorial(n, show=calculo)
