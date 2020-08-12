mai = men = 0
lista = []
for a in range(0, 5):
    lista.append(input(f'Digite um valor para a Posição {a+1}: '))
    if a == 0:
        mai = men = lista[a]
    else:
        if lista[a] > mai:
            mai = lista[a]
        if lista[a] < men:
            men = lista[a]


print(f'Os valores digitados foram {sorted(lista)}')
print(f'O maior número é {mai} que está nas posições', end=' ')
for i, v in enumerate(lista):
    if v == mai:
        print(f'{i}...', end=' ')
print(f'\nO menor número é {men} que está na posições', end=' ')
for i, v in enumerate(lista):
    if v == men:
        print(f'{i}...', end=' ')
