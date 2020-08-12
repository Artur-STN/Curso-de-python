print('Para saber a quantidade de tinta será nescessaria para pintar a parede responda:')
alt = float(input('Qual é a altura da parede em metros: '))
lar = float(input('Qual é a largura da parede em metros: '))
area = alt * lar
tinta = area / 2
print('Sua parede tem a dimensão de {} metros x {} metros ,e sua área é de {:.2f} m²'.format(alt, lar, alt * lar))
print('Para pintar a parede de {:.2f} m² é nescessario {:.0f} litros de tinta'.format(area, tinta))
