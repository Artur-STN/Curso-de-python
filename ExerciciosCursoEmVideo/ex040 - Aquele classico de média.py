n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda Nota: '))
n3 = float(input('Terceira Nota: '))
n4 = float(input('Quarta Nota: '))
m = (n1 + n2 + n3 + n4) / 4

if m <= 4.9:
    print('Média do aluno: {:.1f} .'.format(m))
    print('{}O aluno foi REPROVADO.{}'.format('\033[31m', '\033[m'))
elif 5.0 <= m <= 6.9:
    print('Média do aluno: {:.1f} .'.format(m))
    print('{}O aluno está de RECUPERAÇÂO.{}'.format('\033[33m', '\033[m'))
elif m >= 7.0:
    print('Média do alno: {:.1f} .'.format(m))
    print('{}O aluno foi APROVADO.{}'.format('\033[32m', '\033[m'))
