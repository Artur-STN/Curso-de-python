# função mensagem
def mensagem(txt):
    tam = len(txt) + 4
    print('~' * tam)
    print(f'  {txt}')
    print('~' * tam)


# função se quer continuar
def quercontinuar():
    while True:
        mensagem(str(input('Digite uma frase: ')).upper())
        qc = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
        while qc not in 'SN':
            qc = str(input('Resposta ívalida.\nDigite "S" para Sim ou "N" para Não.'
                           '\nDeseja continuar? [S/N] ')).strip().upper()[0]
        if qc == 'N':
            print(f'{"PROGRAMA FINALIZADO":-^30}')
            break


# programa principal
quercontinuar()
