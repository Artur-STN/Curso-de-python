from datetime import date
anoAtual = date.today().year
totMe = 0
totMa = 0
for pess in range(1, 8):
    Nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(pess)))
    idade = anoAtual - Nasc
    if idade >= 21:
        totMa += 1
    elif idade < 21:
        totMe += 1
print('')
print('Ao todo {} pessoas são maior de idade.'.format(totMa))
print('Ao todo {} pessoas são menor de idade .'.format(totMe))
