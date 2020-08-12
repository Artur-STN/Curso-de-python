from random import randint
pc = randint(0, 10)
tentativas = 1
print('\033[36;1m▼\033[m'*20)
print('''{}Sou o seu computador...{}
{}Acabei de pensar em um número de 0 a 10.{}
{}Você consegue descobrir qual foi?{} '''.format('\033[31;1m', '\033[m', '\033[32;1m', '\033[m', '\033[33;1m', '\033[m'))
print('\033[36;1m▼\033[m'*20)
palpite = int(input('{}Qual é o seu palpite? {}'.format('\033[35;1m', '\033[m')))
print('\033[36;1m▼\033[m'*20)
while pc != palpite:
    if pc > palpite:
        print('\033[36;1m▼\033[m' * 20)
        print('{}Mais... Tente novamente.{}'.format('\033[31;1m', '\033[m'))
        print('\033[36;1m▼\033[m' * 20)
        palpite = int(input('{}Qual é o seu palpite? {}'.format('\033[35;1m', '\033[m')))
    elif palpite > pc:
        print('\033[36;1m▼\033[m' * 20)
        print('{}Menos... Tente novamente.{}'.format('\033[31;1m', '\033[m'))
        print('\033[36;1m▼\033[m' * 20)
        palpite = int(input('{}Qual é o seu palpite? {}'.format('\033[35;1m', '\033[m')))
    tentativas += 1
if tentativas == 1:
    print('\033[36;1m▼\033[m' * 20)
    print('''{}VOCÊ ACERTOU SÓ COM UMA TENTATIVA!! PARABÉNS!!
EU PENSEI NO NÚMERO {}.
    {}'''.format('\033[32m', pc, '\033[m'))
elif pc == palpite:
    print('\033[36;1m▼\033[m' * 20)
    print('''{}Você acertou.
Eu pensei no número {}.
E você descobriu com {} tentativas. Parabéns.{}'''.format('\033[32m', pc, tentativas, '\033[m'))
