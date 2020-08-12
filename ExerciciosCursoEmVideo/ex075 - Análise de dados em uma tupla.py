n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
sn1p = n1 % 2
sn2p = n2 % 2
sn3p = n3 % 2
sn4p = n4 % 2
lista = n1, n2, n3, n4
listPar = []
noveDigt = 0
if n1 == 9 or n2 == 9 or n3 == 9 or n4 == 9:
    noveDigt = lista.count(9)
tresPos = 0
if n1 == 3 or n2 == 3 or n3 == 3 or n4 == 3:
    tresPos = lista.index(3)+1

print('Você digitou os números ', end='')
for a in lista:
    print(a, end=' ')
print(f'\nO valor 9 foi digitado {noveDigt} vezes.')
if tresPos == 0:
    tresPos = 'Nenhuma Posição'
    print(f'O valor 3 apareceu em {tresPos}.')
else:
    print(f'O valor 3 apareceu na posição {tresPos}ª.')
if sn1p == 0:
    listPar += [sn1p]
if sn2p == 0:
    listPar += [sn2p]
if sn3p == 0:
    listPar += [sn3p]
if sn4p == 0:
    listPar += [sn4p]
print(f'O total de valores pares é de {len(listPar)}.')
