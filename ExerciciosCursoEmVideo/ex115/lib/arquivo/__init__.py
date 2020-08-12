from ex115.lib.interface import cabeçalho


def arquivoExiste(nome_do_arquivo):
    try:
        a = open(nome_do_arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome_do_arquivo):
    try:
        a = open(nome_do_arquivo, 'wt+')
        a.close()
    except:
        print('\033[31;1mHove um erro na criação do arquivo!\033[m')
    else:
        print(f'\033[32;1mArquivo {nome_do_arquivo} criado com sucesso!\033[m')


def lerArquivo(nome_do_arquivo):
    try:
        a = open(nome_do_arquivo, 'rt')
    except:
        print(f'\033[31;1mErro ao ler o arquivo {nome_do_arquivo}')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} Anos.')
    finally:
        a.close()


def cadastrar(arquivo, nome='desconhecido', idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print(f'\033[31;1mHouve um erro na arbetura no arquivo {arquivo}!\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31;1mHouve um erro na criação dos dados!')
        else:
            print(f'\033[32;1mNovo de registro de \033[31;1m{nome}\033[m\033[32;1m adicionado.\033[m')
            a.close()
