print('\033[35m=\033[m' * 20)
print(' {}MERCADINHO DO ARTUR{} '.format('\033[32m', '\033[m'))
print('\033[35m=\033[m' * 20)
preço = float(input('{}Qual é o valor total da compra? R$ {}'.format('\033[32m', '\033[m')))
print('''{}FORMA DE PAGAMENTO{}
{}[ 1 ] à vista dinheiro/cheque{}
{}[ 2 ] à vista no cartão{}
{}[ 3 ] 2x no cartão{}
{}[ 4 ] 3x ou mais no cartão{}'''.format('\033[35m', '\033[m', '\033[31m', '\033[m', '\033[32m', '\033[m', '\033[33m',
                                         '\033[m', '\033[34m', '\033[m'))

formapg = int(input('{}Digite a sua opção: {}'.format('\033[35m', '\033[m')))
print('\033[35m=\033[m' * 20)
opcao1 = preço - (preço * 10 / 100)
opcao2 = preço - (preço * 5 / 100)
opcao3 = preço / 2

if formapg == 1:
    print('{}O valor da sua compra de R$ {:.2f} terá um desconto de 10% e vai custar R$ {:.2f} .{}'.format('\033[31m',
                                                                                                           preço,
                                                                                                           opcao1,
                                                                                                           '\033[m'))
elif formapg == 2:
    print('{}O valor da sua compra de R$ {:.2f} terá um desconto de 5% e vai custar R$ {:.2f} .{}'.format('\033[32m',
                                                                                                          preço,
                                                                                                          opcao2,
                                                                                                          '\033[m'))
elif formapg == 3:
    print('{}O pagamento será feito em duas parcelas de R$ {:.2f} totalizando R$ {:.2f} .{}'.format('\033[33m', opcao3,
                                                                                                    opcao3 * 2,
                                                                                                    '\033[m'))
elif formapg == 4:
    parcelas = int(input('{}Quantas parcelas? {}'.format('\033[35m', '\033[m')))
    opcao4: float = (preço * 1.20) / parcelas
    print('\033[35m=\033[m' * 20)
    print(
        '{}O pagamento será feito em {} parcelas de R$ {:.2f}\nTotalizando R$ {:.2f} COM JUROS DE 20 %.{}'.format(
            '\033[34m', parcelas,
            opcao4,
            preço * 1.20,
            '\033[m'))
else:
    print('{}Opção Invalida, Tente novamente!{}'.format('\033[31m', '\033[m'))
