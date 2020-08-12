from ex109 import moeda

p = float(input('Digite o preço: R$ '))
moeda.linha()
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}.')
moeda.linha()
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}.')
moeda.linha()
print(f'Aumentando 10% de {moeda.moeda(p)} , temos {moeda.aumentar(p,10, True)}.')
moeda.linha()
print(f'Diminuindo 13% de {moeda.moeda(p)} , temos {moeda.diminuir(p, 13, True)}.')
moeda.linha()
