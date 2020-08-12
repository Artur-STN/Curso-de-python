lista = []
while True:
    num = int(input('\033[34;1mDigite um valor:\033[m '))
    if num in lista:
        print('\033[31;1mValor duplicado. Não vou adicionar...\033[m')
    else:
        print('\033[32;1mValor adicionado com sucesso...\033[m')
        lista.append(num)
    cont = str(input('\033[34;1mQuer continuar? [S/N]\033[m ')).upper().strip()[0]
    while cont not in 'SN':
        cont = str(input('\033[31;1mDigito Ínvalido, Porfavor digite "S" para Sim ou "N" para Não.\033[m'
                         '\n\033[34;1mQuer continuar? [S/N]\033[m ')) \
            .upper().strip()

    if cont == 'N':
        break
lista.sort()
if len(lista) == 1:
    print(f'\033[36;1mVoçe digitou o valor: {lista}')
else:
    print(f'\033[36;1mVocê digitou os valores: {lista}.')

