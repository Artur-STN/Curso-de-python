from ex108 import moeda

p = float(input('Digite o preço: R$ '))
moeda.linha()
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}.')
moeda.linha()
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}.')
moeda.linha()
print(f'Aumentando 10% de {moeda.moeda(p)} , temos {moeda.moeda(moeda.aumentar(p,10))}.')
moeda.linha()
