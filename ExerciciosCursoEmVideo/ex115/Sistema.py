from time import sleep
from ex115.lib.arquivo import *
from ex115.lib.interface import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

cabeçalho('Sistema Arquivo v1.0')
while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoas', 'Sair do Programa'])
    if resposta == 1:
        # OPÇÃO DE LISTAR UM ARQUIVO
        lerArquivo(arq)

    elif resposta == 2:
        # OPÇÃO DE CADASTRAR UMA NOVA PESSOA
        cabeçalho('NOVO CADASTRO')
        nome = str(input('\033[34;1mNome:\033[m '))
        idade = leiaInt('\033[34;1mIdade:\033[m ')
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        cabeçalho('Saindo do programa.')
        sleep(1)
        break
    else:
        cabeçalho('\033[31;1mERRO! Digite um Opção válida.\033[m')
    sleep(2)
