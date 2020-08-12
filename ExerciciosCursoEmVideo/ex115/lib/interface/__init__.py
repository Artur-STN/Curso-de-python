# ---------- VARIAVAL TAMANHO ---------- #
tamGeral = 42


def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31;1mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[1;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return valor


def linha(tam=tamGeral):
    print('\033[36;1m-\033[m' * tam)


def cabeçalho(txt):
    linha()
    print('\033[32;1m', txt.center(tamGeral), '\033[m')
    linha()


def menu(lista):
    cabeçalho('MENU PRINCIPAl'.center(tamGeral))
    c = 1
    for item in lista:
        print(f'\033[32;1m{c} - \033[34;1m{item}\033[m')
        c += 1
    linha()
    opc = leiaInt('\033[32;1mSua Opção: ')
    return opc
