dados = dict()
gols = list()
dados['nome'] = str(input('Nome do jogador: ')).title().strip()
jogos = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range(jogos):
    gols.append(int(input(f'Quantos gols na {c + 1}ª partida? ')))
dados['SomaGols'] = sum(gols)
dados['gols'] = gols.copy()
print('▲' * 30)
print(dados)
print('▲' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}.')
print('▲' * 30)
print(f'O jogador {dados["nome"]} jogou {jogos}.')
for partida, gol in enumerate(dados['gols']):
    print(f'     → Na {partida+1}ª partida, fez {gol} gol(s).')
print(f'Foi um total de {dados["SomaGols"]}.')
