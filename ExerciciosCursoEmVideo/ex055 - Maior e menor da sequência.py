lista = []
for a in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(a)))
    lista += [peso]
print('A pessoa mais pessada pessa {} .'.format(max(lista)))
print('A pessoa menos leve pessa {} .'.format(min(lista)))
