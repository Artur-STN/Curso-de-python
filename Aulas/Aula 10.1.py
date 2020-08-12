nome = str(input('Qual é o seu nome? ')).title().strip()
separa = nome.split()
print('Bom Dia,Senhor {}!.'.format(separa[0]))
if separa[0] == 'Artur':
    print('Seja Bem Vindo de volta Senhor {}.'.format(separa[0]))
else:
    print('Quem é você?!')
