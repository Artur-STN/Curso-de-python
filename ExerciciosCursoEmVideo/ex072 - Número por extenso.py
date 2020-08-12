todos = (
    'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
    'Quatorze', 'Quinze', 'Dezesseis', 'Dezesete', 'Dezoito', 'Dezenove', 'vinte')

while True:
    while True:
        num = int(input('Digite um número de 0 a 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente. ', end='')
    print(f'Você digitou o número {num} que por extenso é: {todos[num]}')
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        print('Volte Sempre!')
        break
