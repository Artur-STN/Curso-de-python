temp = list()
princ = list()
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')).title())
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    princ.append(temp[:])
    temp.clear()
    qc = str(input('Quer continuar? [S/N] ')).upper().strip()
    while qc not in 'SN':
        qc = str(input('Quer continuar? [S/N] ')).upper().strip()
    if qc == 'N':
        break
print('-=-'*30)
print(f'{len(princ)} pessoas foram cadastradas.')
print(f'O maior peso é de {maior}Kg. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso é de {menor}Kg. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
