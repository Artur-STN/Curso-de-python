def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31;1mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[1;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return valor


def leiaFloat(msg):
    while True:
        try:
            valor = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31;1mERRO! Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[1;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return valor


# Programa Principal
inteiro = leiaInt('\033[35;1mDigite um número interio: ')
real = leiaFloat('\033[35;1mDigite um número Real: ')
print(f'\033[33;1mO número Interio digitado foi {inteiro} e o número Real digitado foi {real}.')
