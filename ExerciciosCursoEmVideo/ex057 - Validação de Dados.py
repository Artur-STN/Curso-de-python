sexo = str(input('Qual é o seu sexo? (M/F) ')).upper().strip()
while sexo not in 'MF':
    sexo = str(
        input('Dados inválidos. Por favor, informe "M" para Masculino ou "F" para Feminino seu sexo? (M/F) ')).upper()\
        .strip()
if sexo in 'MF':
    if sexo == 'M':
        M = 'Masculino'
        print('Sexo {} registrado com sucesso'.format(M))
    elif sexo == 'F':
        F = 'Feminino'
        print('Sexo {} registrado com sucesso'.format(F))

