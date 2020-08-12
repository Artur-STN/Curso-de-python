soma = 0
for pares in range(1, 7):
    num = int(input('Digite {}° valor: '.format(pares)))
    np = num % 2
    if num % 2 == 0:
        soma += num
print(' ')
print('Você informou {} números pares e a soma deles é {}'.format(np, soma))
