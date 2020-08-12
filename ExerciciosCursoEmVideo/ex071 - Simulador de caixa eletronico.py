print('=' * 45)
print('{:^45}'.format('BANCO CEV'))
print('=' * 45)
valor = int(input('Qual o valor que você quer sacar? R$ '))
ced = 50
totced = 0
while True:
    if valor >= ced:
        valor -= ced
        totced += 1
    else:
        print(f'Total {totced} de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if valor == 0:
            break
print('=' * 45)
print('{:^45}'.format('VOLTE SEMPRE AO BANCO CEV. TENHA UM BOM DIA!'))
print('=' * 45)
