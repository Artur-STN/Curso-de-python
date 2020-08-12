maioridadehomem = 0
somaidade = 0
nomevelho = ''
totmulher20 = 0
for pessoas in range(1, 5):
    print('----- {}ª PESSOA -----'.format(pessoas))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (M ou F): ')).upper().strip()
    somaidade += idade
    if pessoas == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade > 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('Homem mais velho tem {} e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))
