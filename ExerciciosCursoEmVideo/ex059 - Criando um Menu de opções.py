from time import sleep
print('\033[31;1m▲▼\033[m'*10)
n1 = int(input('{}Primeiro valor: {}'.format('\033[32;1m', '\033[m')))
n2 = int(input('{}Segundo valor: {}'.format('\033[33;1m', '\033[m')))
print('\033[31;1m▲▼\033[m'*10)
sair = 0
maior = [n1, n2]

while sair != 5:
    print('''{}     [ 1 ] Somar{}
     {}[ 2 ] Multiplicar{}
     {}[ 3 ] Maior{}
     {}[ 4 ] Novos Números{}
     {}[ 5 ] Sair do Programa{}'''.format('\033[32;1m', '\033[m', '\033[33;1m', '\033[m', '\033[34;1m', '\033[m',
                                     '\033[35;1m', '\033[m', '\033[36;1m', '\033[m'))
    print('\033[31;1m▲▼\033[m' * 10)
    opcao = int(input('{}Digite a sua opção: {}'.format('\033[30;1m', '\033[m')))
    print('\033[31;1m▲▼\033[m' * 10)
    if opcao == 1:
        print('{}A soma é: {} + {} = {}{}'.format('\033[32;1m', n1, n2, n1 + n2, '\033[m'))
    elif opcao == 2:
        print('{}O produto de {} X {} = {}{}'.format('\033[33;1m', n1, n2, n1 * n2, '\033[m'))
    elif opcao == 3:
        print('{}Entre {} e {} o maior é {}{}'.format('\033[34;1m', n1, n2, max(maior), '\033[m'))
    elif opcao == 4:
        print('{}Informe os novos valores.{}'.format('\033[35;1m', '\033[m'))
        n1 = int(input('{}Primeiro valor: {}'.format('\033[32;1m', '\033[m')))
        n2 = int(input('{}Segundo valor: {}'.format('\033[33;1m', '\033[m')))
    elif opcao > 5:
        print('{}Opção inválida. Tente novamente.{}'.format('\033[31;1m', '\033[m'))
    print('\033[31;1m▲▼\033[m' * 10)
    if opcao == 5:
            print('{}Finalizando...{}'.format('\033[36;1m', '\033[m')), sleep(2)
            print('{}Fim do Programa! Volte Sempre!{}'.format('\033[36;1m', '\033[m'))
            sair = 5
