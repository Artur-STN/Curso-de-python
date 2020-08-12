lista = []
while True:
    print('\033[34;1m▼\033[m' * 30)
    produto = str(input('\033[32;1mDigite o produto:\033[m ')).strip().title()
    print('\033[34;1m▲\033[m' * 30)
    lista += [produto]
    print('\033[34;1m▼\033[m' * 30)
    preco = float(input('\033[32;1mDigite o preço do produto: R$\033[m '))
    print('\033[34;1m▲\033[m' * 30)
    lista += [preco]
    print('\033[34;1m▼\033[m' * 30)
    cont = str(input('\033[32;1mQuer continuar? [S/N]\033[m ')).upper().strip()
    print('\033[34;1m▲\033[m' * 30)
    while cont not in 'SN':
        print('\033[34;1m▼\033[m' * 30)
        cont = str(input('\033[31;1mDigito Ínvalido, Porfavor digite "S" para Sim ou "N" para Não.\033[m'
                         '\n\033[32;1mQuer continuar? [S/N]\033[m '))\
            .upper().strip()
        print('\033[34;1m▲\033[m' * 30)
    if cont == 'N':
        break
print('\033[34;1m▼\033[m'*30)
print('{:^65}'.format('\033[30;1m LISTAGEM D\033[36;1mE PRODUTOS\033[m'))
for tabela in range(0, len(lista), 2):
    print(f'\033[30;1m{lista[tabela]:.<30}\033[m \033[36;1mR${lista[tabela+1]:>7.2f}')
print('\033[34;1m▲\033[m'*30)
