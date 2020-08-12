from datetime import date
anoAtual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = anoAtual - nasc
alis = anoAtual - (nasc + 18)
anoQvaiAlistar = nasc + 18
print('{}Quem nasceu em {} tem {} anos em {}{}.'.format('\033[32m', nasc, idade, anoAtual,  '\033[m'))
if idade > 18:
    print('{}Você deveria se alistar há {} anos.{}'.format('\033[31m', alis, '\033[m'))
    print('{}Corra atrás do seu alismento com URGÊNCIA{}'.format('\033[31m', '\033[m'))
elif idade < 18:
    print('{}O ano do seu alistamento será em {}.{}'.format('\033[33m', anoQvaiAlistar,  '\033[m'))
    print('{}Fique atento para o ano do seu alistamento!!{}'.format('\033[33m',  '\033[m'))
else:
    print('{}Você deve se alistar IMEDIATAMENTE!'.format('\033[31m'))
