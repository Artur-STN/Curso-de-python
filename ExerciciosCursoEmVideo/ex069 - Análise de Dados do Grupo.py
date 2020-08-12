quantH = mulheresMenos20 = mais18 = 0
while True:
    idade = int(input('Idade: '))
    if idade < 0:
        while idade < 0:
            print('É impossível alguém ter idade negativa!')
            print('---' * 5)
            idade = int(input('Digite a idade: '))
    if idade > 130:
        while idade > 130:
            print('Tem certeza que essa pessoa tem mais de 130 anos??')
            print('---' * 5)
            idade = int(input('Digite a idade real: '))
    sexo = str(input('Sexo [S/N]: ')).upper()[0]
    while sexo not in 'MF':
        print('Você digitou uma opção INVÁLIDA, digite novamente.')
        sexo = str(input('Sexo [S/N]: ')).upper()[0]
    continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper()[0]
    if idade >= 18:
        mais18 += 1
    elif sexo == 'M':
        quantH += 1
    elif sexo == 'F' and idade < 20:
        mulheresMenos20 += 1
    if continuar == 'N':
        break
print(f'''Total de pessoas com mais de 18 anos: {mais18}
Total de homens cadastrados: {quantH}
Total de mulheres com menos de 20 anos: {mulheresMenos20}''')
