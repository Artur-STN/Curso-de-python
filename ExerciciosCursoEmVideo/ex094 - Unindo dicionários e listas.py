dados = dict()
pessoas = list()
TotPessoas = TotIdade = TotMulheres = 0

while True:
    dados["nome"] = str(input('Nome: ')).title().strip()
    TotPessoas += 1
    sexo = str(input('Sexo: [F/M] ')).strip().upper()[0]
    while sexo not in 'FM':
        sexo = str(input('Resposta ívalida.\nDigite "F" para Feminino ou "M" para Masculino.\nSexo: [F/M] ')).strip(
        ).upper()[0]
    if sexo == 'F':
        dados['sexo'] = 'Feminino'
        TotMulheres += 1
    elif sexo == 'M':
        dados['sexo'] = 'Masculino'
    dados['idade'] = int(input('Idade: '))
    TotIdade += dados['idade']
    MediaIdade = TotIdade / TotPessoas
    pessoas.append(dados.copy())
    qc = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    while qc not in 'SN':
        qc = str(input('Resposta ívalida.\nDigite "S" para Sim ou "N" para Não.'
                       '\nDeseja continuar? [S/N] ')).strip().upper()[0]
    if qc == 'N':
        break
print('▲' * 30)
if TotPessoas == 1:
    print(f'Uma pessoa foi cadastrada.')
else:
    print(f'A) O grupo tem {TotPessoas} pessoa(s).')
    print(f'B) A média de idade do grupo é de {MediaIdade:.2f} anos.')
if TotMulheres > 1:
    print('C) As mulheres cadastradas foram ', end='')
    for dados in pessoas:
        if dados['sexo'] == 'Feminino':
            print(f'{dados["nome"]}', end=' ')
    print('.')
else:
    print('C) A única mulher cadastradas foi ', end='')
    for dados in pessoas:
        if dados['sexo'] == 'Feminino':
            print(f'{dados["nome"]}.')

print(f'D) Lista de pessoas com a idade acima da média:')
for dados in pessoas:
    if dados['idade'] > MediaIdade:
        print(end='    =>  ')
        print(f'{dados["nome"]} = {dados["idade"]} ', end='\n')
