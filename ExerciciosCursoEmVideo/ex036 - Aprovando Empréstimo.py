# casa = valor da casa
# sc salario do comprador
# af = anos do financiamento
# pres = prestação mensal
print('{}ATENÇÃO, O VALOR DO EMPRÉSTIMO NÃO PASSAR DE 30 % DO SALÁRIO.{}'.format('\033[31m', '\033[m'))
casa = float(input('Qual é o valor da casa: R$ '))
s = float(input('Qual é o salário do comprador: R$ '))
af = int(input('Quantos anos de financiamento? '))
pres = float(casa / (af * 12))
sal = s * 30 / 100
print(' ')
if pres <= sal:
    print('30 % do salário é R$ {:.2f} .'.format(sal))
    print('Para pagar uma casa de R$ {:.2f} em {} anos, a prestação será de R$ {:.2f}'.format(casa, af, pres))
    print('{}Seu emprestimo está aprovado!{}'.format('\033[32m', '\033[m'))
else:
    print('30 % do salário é R$ {:.2f} .'.format(sal))
    print('Para pagar uma casa de R$ {:.2f} em {} anos, a prestação será de R$ {:.2f}'.format(casa, af, pres))
    print('{}Seu emprestimo está Negado!{}'.format('\033[31m', '\033[m'))
