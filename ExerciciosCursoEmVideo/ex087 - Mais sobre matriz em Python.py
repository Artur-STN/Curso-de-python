matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for x in range(0, 3):
    for c in range(0, 3):
        matriz[x][c] = (int(input(f'Digite valor para a posição [{x}, {c}]: ')))
        if matriz[x][c] % 2 == 0:
            spar += matriz[x][c]
print('-=-'*10)
for x in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[x][c]:^7}]', end='')
    print()
print('-=-'*10)
print(f'A soma dos valores pares é {spar}.')
for x in range(0, 3):
    scol += matriz[x][2]
print(f'A soma dos vlores da terceira coluna é {scol}.')
for c in range(0, 3):
    if c == 0 or matriz[1][c] > mai:
        mai = matriz[1][c]
print(f'A soma dos valores da segunda linha é {mai}.')
