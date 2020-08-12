# pessoas = {'Nome': 'Artur', 'Idade': 19, 'Sexo': 'Masculino'}
# print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos.')
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())
# del pessoas['Sexo']
# pessoas['Nome'] = 'Marcio'
# pessoas['Peso'] = 98.5
# for k, v in pessoas.items():
#     print(f'{k:<5} = {v:<5}')

# Brasil = list()
# Estado_1 = {'UF': 'Rio de Janeiro', 'Sigla': 'RJ'}
# Estado_2 = {'UF': 'São Paulo', 'Sigla': 'SP'}
# Brasil.append(Estado_1)
# Brasil.append(Estado_2)
# print(Estado_1)
# print(Estado_2)
# print(Brasil)
# print(Brasil[0])
# print(Brasil[1])
# print(Brasil[0]['UF'])
# print(Brasil[1]['UF'])
# print(Brasil[0]['Sigla'])
# print(Brasil[1]['Sigla'])

estado = dict()
brasil = list()
for c in range(3):
    estado['UF'] = str(input('Unidade Federativa: '))
    estado['Sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    # for k, v in e.items():
    #     print(f'O campo {k} tem valor {v}.')
    for v in e.values():
        print(v, end=' ')
