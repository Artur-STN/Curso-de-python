n1 = float(input('Nota do Primeiro Trimestre: '))
n2 = float(input('Nota do Segundo Trimestre: '))
n3 = float(input('Nota do Terceiro Trimestre: '))
n4 = float(input('Nota do Quarto Trimestre: '))
m = (n1 + n2 + n3 + n4) / 4
print('Sua média foi {:.1f}'.format(m))
if m >= 6:
    print('Média Boa.')
else:
    print('Média Ruim.')
