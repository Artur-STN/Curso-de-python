aluno = dict()
aluno['nome'] = str(input('\033[34;1mNome: ')).title().strip()
aluno['Média'] = float(input(f'\033[34;1mMédia de {aluno["nome"]}: '))
aluno['Situação'] = ''
if aluno['Média'] >= 7:
    aluno['Situação'] = '\033[32;1mAprovado'
elif aluno['Média'] >= 5:
    aluno['Situação'] = '\033[33;1mRecuperação'
else:
    aluno['Situação'] = '\033[31;1mReprovado'
print(f'\033[34;1m{"Nome":<20}\033[35;1m|\033[34;1m{"Média":<15}\033[35;1m|\033[34;1m{"Situação":<16}\033[m')
print(f'\033[36;1m{aluno["nome"]:<20}\033[35;1m|\033[36;1m{aluno["Média"]:<15.2f}\033[35;1m|'
      f'\033[36;1m{aluno["Situação"]:<20}')
