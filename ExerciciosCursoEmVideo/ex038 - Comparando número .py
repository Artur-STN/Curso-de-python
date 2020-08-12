n1 = int(input('{}Digite um número inteiro:{} '.format('\033[31m', '\033[m')))
n2 = int(input('{}Digite um segundo número inteiro:{} '.format('\033[32m', '\033[m')))
if n1 > n2:
    print('{}O número {} é maior{}'.format('\033[33m', n1, '\033[m'))
elif n2 > n1:
    print('{}O número {} é maior'.format('\033[33m', n2))
else:
    print('{}{}Não exite um número maior, pois os dois são iguais.{}'.format('\033[m', '\033[31m', '\033[m'))
