def SeVota(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    print(f'Com {idade} anos: ')
    if idade == 16 or idade == 17 or idade > 65:
        return print('\033[33;1mVoto Opcional.')
    elif 18 <= idade <= 70:
        return print('\033[31;1mVoto Obrigatorio.')
    elif idade < 16:
        return print('\033[32;1mNão Vota.')


# Programa Principal
nasc = int(input('\033[35;1mEm que ano você nasceu? '))
SeVota(nasc)
