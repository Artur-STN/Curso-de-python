time = list()
dados = dict()
gols = list()
while True:
    print('▲' * 40)
    dados.clear()
    dados['nome'] = str(input('Nome do jogador: ')).title().strip()
    jogos = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    gols.clear()
    for c in range(jogos):
        gols.append(int(input(f'Quantos gols na {c + 1}ª partida? ')))
    dados['SomaGols'] = sum(gols)
    dados['gols'] = gols.copy()
    time.append(dados.copy())
    qc = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while qc not in 'SN':
        qc = str(input('Resposta ívalida.\nDigite "S" para Sim ou "N" para Não.'
                       '\nDeseja continuar? [S/N] ')).strip().upper()[0]
    if qc == 'N':
        break
print('▲' * 40)
print(' Cod', end='')
print(f'{"":^2}{"Nome":<13}{"Total de Gols":<13}{"Gols":^13}', end='')
print()
print('▲' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} - ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('▲' * 30)
while True:
    busca = int(input('Deseja ver os dados de qual jogador? (Digite 999 para parar.) '))
    if busca == 999:
        print('▲' * 30)
        print(f'{"":<10}{"PROGRAMA FINALIZADO":-^30}{"":>10}')
        break
    if busca >= len(time):
        if len(time) == 1:
            print('▲' * 30)
            print(f'Erro! É possivel buscar somente dados do jogador 0.')
        elif len(time) > 0:
            print('▲' * 30)
            print(f'Erro! Digite um valor entre 0 até {len(time)-1}.')
    elif busca < len(time) or busca == 0:
        print('▲' * 30)
        print(f'O jogador {time[busca]["nome"]} jogou {len(time[busca]["gols"])} jogos.')
        for partida, gol in enumerate(time[busca]["gols"]):
            print(f'     → Na {partida+1}ª partida, fez {gol} gol(s).')
        print(f'Foi um total de {time[busca]["SomaGols"]} gols.')
        print('▲' * 30)
