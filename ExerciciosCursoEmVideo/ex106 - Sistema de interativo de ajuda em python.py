from time import sleep


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'.', cor='azul')
    sleep(1)
    print(cores['branco'])
    help(com)
    print(cores['sem'])


def titulo(msg, cor='sem'):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'| {msg} |')
    print('~' * tam)
    print(cores['sem'], end='')


# Programa Principal
cores = {'sem': '\033[m',  # Limpa cor
         'vermelho': '\033[30;1;41m',
         'verde': '\033[30;1;42m',
         'azul': '\033[1;44;30m',
         'branco': '\033[7;30m'
         }

while True:
    titulo('SISTEMA DE AJUDA PyHELP', cor='verde')
    codigo = str(input('Função ou Biblioteca > '))
    if codigo.upper() == 'FIM':
        titulo('Até Logo!', cor='vermelho')
        break
    else:
        ajuda(codigo)
