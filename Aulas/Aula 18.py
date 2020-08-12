# teste = list()
# teste.append("Artur")
# teste.append(19)
# galera = list()
# galera.append(teste)
# teste[0] = 'Eduarda'
# teste[1] = 13
# galera.append(teste)
# print(galera)

# teste = list()
# teste.append("Artur")
# teste.append(19)
# galera = list()
# galera.append(teste[:])
# teste[0] = 'Eduarda'
# teste[1] = 13
# galera.append(teste[:])
# print(galera)

# galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
# print(galera[0][0])
# print(galera[2][1])
# print(galera[1][0])
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade.')
#     if p[1] >= 18:
#         print('E é maior de idade.')
#     else:
#         print('E é menor de idade.')
#     print('-=-'*10)

dado = list()
galera = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} tem {p[1]} anos de idade e é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} tem {p[1]} anos de idade e é menor de idade.')
        totmen += 1
print(f'Quantidade de maiores de idade: {totmai}')
print(f'Quantidade de menores de idade: {totmen}')
