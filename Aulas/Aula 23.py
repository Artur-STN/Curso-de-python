# n = int(input('Número: '))
# print(f'Você digitou o número {n}')

try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
# except (ValueError, TypeError):
#     print('Tivemos um problema com os tipos de dados que você digitou.')
# except ZeroDivisionError:
#     print('Não é possivel dividir por zero.')
# except KeyboardInterrupt:
#     print('Algum dados não foi informado.')
except Exception as erro:
    print(f'''Programa \033[31;1mNÂO\033[m foi executado com sucesso.
ERRO: {erro.__class__}''')
else:
    print(f'O resultado da divisão da entre {a} e {b} é {r:.1f}.')
finally:
    print('Volte sempre.')
