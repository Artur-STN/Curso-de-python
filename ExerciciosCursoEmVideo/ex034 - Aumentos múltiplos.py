s = float(input('Qual é o salário do funcionário? R$ '))
sma = s + s * 10 / 100
sme = s + s * 15 / 100

if s <= 1250:
    print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} .'.format(s, sme))
else:
    print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} .'.format(s, sma))
