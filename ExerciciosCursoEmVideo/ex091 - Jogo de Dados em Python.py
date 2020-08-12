from operator import itemgetter
from random import randint
from time import sleep

jogo = {'jogador 1': randint(1, 6),
        'jogador 2': randint(1, 6),
        'jogador 3': randint(1, 6),
        'jogador 4': randint(1, 6)}

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(f'{"Ranking":^15}')
for i, v in enumerate(ranking):
    print(f'N°{i + 1} => {v[0]:<10}- {v[1]:<5}')
    sleep(1)
