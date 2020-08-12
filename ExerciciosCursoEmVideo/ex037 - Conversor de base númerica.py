num =int(input('{}Digite um número inteiro:{} '.format('\033[34m','\033[m')))
print('''{}Escolha uma das bases para a conversão:{} 
{}[ 1 ] para BINÁRIO{}
{}[ 2 ] para OCTAl{}
{}[ 3 ] para HEXADECIMAL{}'''.format('\033[35m', '\033[m', '\033[31m', '\033[m', '\033[32m', '\033[m', '\033[33m', '\033[m'))

opcao = int(input('{}Digite a sua opção:{} '.format('\033[36m', '\033[m')))
if opcao == 1:
    print('{}{} convertido para BINÁRIO é igual a {}{}'.format('\033[31m',num, bin(num)[2:], '\033[m'))
elif opcao == 2:
    print('{}{} convertido para OCTAL é igual a {}{}'.format('\033[32m', num, oct(num)[2:], '\033[m'))
elif opcao == 3:
    print('{}{} convertido para HEXADECIMAL é igual a {}{}'.format('\033[33m', num, hex(num)[2:], '\033[m'))
else:
    print('Opção inválida, Tente novamente.')
