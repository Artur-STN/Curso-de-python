dias = float(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
aluguel = dias * 60 + km * 0.15
print('O total a pagar pelo aluguel é de R$ {:.2f} '.format(aluguel))
