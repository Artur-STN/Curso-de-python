from ex107 import moeda

p = float(input('Digite o preço: R$ '))
moeda.linha()
print(f'A metade de R$ {p:.2f} é R$ {moeda.metade(p):.2f}')
moeda.linha()
print(f'O dobro de R$ {p:.2f} é R$ {moeda.dobro(p):.2f}')
moeda.linha()
print(f'Aumentando 10% de R$ {p:.2f} temos {moeda.aumentar(p,10):.2f}')
moeda.linha()
