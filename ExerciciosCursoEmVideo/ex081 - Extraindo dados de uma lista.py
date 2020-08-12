lista = []
while True:
    lista.append( int(input('Digite um valor: ')))
    qc = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while qc not in 'SN':
        qc = str(input('Digito ínvalido.\nDigite "S" para Sim ou "N" para Não.\nQuer continuar? [S/N] '))\
            .strip().upper()[0]
    if qc == 'N':
        break
print('-='*30)
print(f'Você digitou {len(lista)} números.')
print(f'Os valores digitados foram {sorted(lista, reverse= True)}')
if 5 in lista:
    sorted(lista, reverse=False)
    print(f'O valor 5 foi encotrado na lista na posição {lista.index(5)}!')
else:
    print('O valor 5 não foi encontrado na lista!')
