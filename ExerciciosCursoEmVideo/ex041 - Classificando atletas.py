from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('O Atleta tem {} anos.'.format(idade))
if 0 == idade >= 9:
    print('E é classificado como: MIRIM')
elif 10 >= idade >= 14:
    print('E é classificado como: INFANTIL')
elif 15 >= idade >= 19:
    print('E é classificado como: JUNIOR')
elif 20 >= idade >= 25:
    print('E é classificado como: SÊNIOR')
else:
    print('E é classificado como: MASTER')