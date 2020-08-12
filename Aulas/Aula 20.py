# from random import randint
#
#
# def linha():
#     print('-' * 30)
#
#
# def soma(a, b):
#     print(f'A = {a} e B = {b}')
#     s = a + b
#     print(f'A soma A + B = {s}')
#
#
# Programa principal
# linha()
# soma(randint(1, 100), randint(1, 100))
# linha()
# soma(randint(1, 100), randint(1, 100))
# linha()
# soma(randint(1, 100), randint(1, 100))
# linha()
# soma(randint(1, 100), randint(1, 100))
# linha()


# def contador(*núm):
#     for valor in núm:
#         print(valor, end=' - ')
#     print('END')
#     tamanho = len(núm)
#     print(f'Recebi os valóres {núm} que são ao todo {tamanho} números.')
#
#
# contador(2, 1, 7)
# contador(8, 0)
# contador(4, 4, 7, 6, 2)

# def dobra(lista):
#     pos = 0
#     while pos < len(lista):
#         lista[pos] *= 2
#         pos += 1
#
#
# valores = [4, 25, 0, 4, 8]
# dobra(valores)
# print(valores)

def soma(*valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somandos os valores {valores} temos {s}.')


soma(5, 3, 4)
soma(8, 6)
