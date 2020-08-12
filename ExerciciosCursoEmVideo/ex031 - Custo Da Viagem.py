# km = Quilometros
# p = preço
# pp = preço com promoção
# d = diferença de pp para p
km = float(input('Qual é a distância da viagem em quilometros? '))
print('Você está prestes a começar uma viagem de {} km.'.format(km))
p = km * 0.50
pp = km * 0.45
d = p - pp
if km >= 200:
    print('O preço da passagem terá promoção de R$ {:.2f} , e será R$ {:.2f} .'.format(d, pp))
else:
    print('Sua passagem será de R$ {:.2f} .'.format(pp))
