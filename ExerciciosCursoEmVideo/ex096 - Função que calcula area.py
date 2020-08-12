# Função Linha
def linha():
    print('-' * 30)


# Função área
def área():
    largura = float(input('Largura: (Metros) '))
    altura = float(input('Altura: (Metros) '))
    area = altura * largura
    linha()
    print(f'A área do terredo de {largura:.1f} X {altura:.1f} é de {area:.1f} m².')


# Programa Principal
print(f'{"Controle De Terrenos":^30}')
linha()
área()
linha()
