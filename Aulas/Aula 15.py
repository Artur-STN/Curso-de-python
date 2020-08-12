from random import randint
n = s = 0
while True:
    n = randint(1, 999)
    print(n)
    if n == 9:
        break
    else:
        s += n
print(f'A soma de todos os números é {s:-^20}')
