times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
         'Atlético', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
         'Bahia', 'Corinthians', 'Fluminense', 'Vasco', 'Ceará-SC',
         'Chapecoense', 'Sport Recife', 'América-MG', 'EC Vitória', 'Paraná')
chape = times.index('Chapecoense')

print('\033[36;1m▲▼\033[m'*10)
print(f'Lista do times do Brasileirão: {times}')
print('\033[36;1m▲▼\033[m'*10)
print(f'Times em ordem alfabética: {sorted(times)}')
print('\033[36;1m▲▼\033[m'*10)
print(f'Os 5 primeiros times são : {times[:6]}')
print('\033[36;1m▲▼\033[m'*10)
print(f'Os 4 últimos são {times[-4:]}')
print('\033[36;1m▲▼\033[m'*10)
print(f'A Chapecoense está na posição: {chape + 1}ª')
print('\033[36;1m▲▼\033[m'*10)
