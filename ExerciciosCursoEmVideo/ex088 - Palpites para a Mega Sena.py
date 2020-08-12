from time import sleep
from random import randint
tot = 1
lista = list()
jogos = list()
print('\033[31;1m▲\033[32;1m▼\033[31;1m▲\033[m'*10)
print('{}{:^50}{}'.format('\033[36;1m', 'JOGOS DA MEGA SENA', '\033[m'))
print('\033[31;1m▲\033[32;1m▼\033[31;1m▲\033[m'*10)
quant = int(input('\033[36;1mQuantos jogos você quer que eu sorteie? '))
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('\033[31;1m▲\033[32;1m▼\033[31;1m▲\033[m'*10)
print('{}{:^50}{}'.format('\033[36;1m', f'SORETEANDO {quant} JOGOS', '\033[m'))
print('\033[31;1m▲\033[32;1m▼\033[31;1m▲\033[m'*10)
for i, c in enumerate(jogos):
    print(f'\033[34;1mJogo {i+1} → {c}.')
    sleep(1)
print('\033[31;1m▲\033[32;1m▼\033[31;1m▲\033[m'*10)
