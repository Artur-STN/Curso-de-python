soN = 'S'
media = quant = soma = maior = menor = 0
while soN in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    soN = str(input('Você quer continuar? [S/N] ')).strip()[0].upper()
media = soma / quant
print('''Você digitou {} números e a média é {}.
E o maior número é {} e o menor número é {}'''.format(quant, soma, maior, menor))
