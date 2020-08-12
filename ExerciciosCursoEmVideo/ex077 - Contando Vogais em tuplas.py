words = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON',
         'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR',
         'TRABALHAR', 'MERCADO', 'PROGRAMADOS', 'FUTURO')
for cont in words:
    print(f'\nNa palavra {cont} temos as vogais ', end=' ')
    for letra in cont:
        if letra in 'AEIOU':
            print(letra, end=' ')
