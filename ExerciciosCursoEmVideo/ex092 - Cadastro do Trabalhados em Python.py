from datetime import date
dados = dict()
dados['nome'] = str(input('Nome: ')).strip().title()
dados['Ano_de_Nascimento'] = int(input('Ano de nascimento: '))
AnoAtual = date.today().year
Idade = AnoAtual - dados['Ano_de_Nascimento']
dados['CTPS'] = int(input('Carteira de Trabalho: (Se não tiver digite 0): '))
if dados['CTPS'] == 0:
    print('▲' * 30)
    print(f'Nome: {dados["nome"]} ')
    print(f'Idade: {Idade} ')
    print(f'CTPS: {dados["CTPS"]}')
else:
    dados['Ano_de_Contratação'] = int(input('Ano de Contratação: '))
    dados['Salário'] = int(input('Salário: R$ '))
    print('▲' * 30)
    print(f'Nome: {dados["nome"]} ')
    print(f'Idade: {Idade} ')
    print(f'CTPS: {dados["CTPS"]}')
    print(f'Contratado no ano de {dados["Ano_de_Contratação"]}.')
    print(f'Salário R$ {dados["Salário"]:.2f}.')
    dados['AnoAposento'] = dados['Ano_de_Contratação'] + 35 - dados['Ano_de_Nascimento']
    print(f'Você ira se aposentar com {dados["AnoAposento"]} anos.')

