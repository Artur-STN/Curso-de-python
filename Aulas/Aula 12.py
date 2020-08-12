nome = str(input('Qual é o seu nome? ')).title()
if nome == 'Artur':
    print('Que nome bonito Senhor {}.'.format(nome))
elif nome == '':
    print('Seja Bem Vinda sua feia!')
else:
    print('Olá {} , prazer em conhece - lô.'.format(nome))
print('Tenha um Bom Dia!')
