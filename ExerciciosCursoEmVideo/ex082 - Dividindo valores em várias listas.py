lista = list()
pares = list()
impares = list()
pos = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    if lista[pos] % 2 == 0:
        pares.append(lista[pos])
    else:
        impares.append(lista[pos])
    pos += 1
    qc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while qc not in 'SN':
        qc = str(input('Digito ínvalido.\nDigite "S" para Sim ou "N" para Não.\nQuer continuar? [S/N] '))\
            .strip().upper()[0]
    if qc == 'N':
        break
print('-=-'*10)
print(f'A lista completa é {sorted(lista)}.')
print(f'Os números pares são {sorted(pares)}.')
print(f'OS números ímpares são {sorted(impares)}.')
