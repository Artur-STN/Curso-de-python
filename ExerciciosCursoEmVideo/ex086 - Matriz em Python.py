matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for x in range(0, 3):
    for c in range(0, 3):
        matriz[x][c] = (int(input(f'Digite valor para a posição [{x}, {c}]: ')))
print('-=-'*10)
for x in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[x][c]:^7}]', end='')
    print()
