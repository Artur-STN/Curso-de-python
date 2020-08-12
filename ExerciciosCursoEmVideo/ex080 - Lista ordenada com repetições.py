lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n >= lista[-1]:
        lista.append(n)
        print('Valor adicionado na última posição.')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos}.')
                break
            pos += 1
print('='*30)
print(f'A lista em ordem crescente é {lista}.')
