from random import randint
pc = (randint(0, 10)), (randint(0, 10)), (randint(0, 10)), (randint(0, 10)), (randint(0, 10))
print('Os valores sorteados foram: ', end='')
for a in pc:
    print(f'{a} ', end='')
print(f'\nO Maior valor sorteado foi {max(pc)}.')
print(f'O Menor valor sorteado foi {min(pc)}.')
