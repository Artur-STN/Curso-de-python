def leiaInt(num):
    while True:
        valor = str(input(num))
        if valor.isnumeric():
            return valor
        else:
            print('\033[31;1mERRO! Digite um número inteiro valido.\033[m')
        if valor.isnumeric():
            break


# Programa Principal
n = leiaInt('\033[35;1mDigite um número: ')
print(f'\033[33;1mVocê digitou o número {n}.')
