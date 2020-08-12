galera = []
dados = []

while True:
    dados.append(str(input('Nome: ')).strip().title())

    for notas in range(4):
        dados.append(float(input(f'Nota {notas+1}: ')))

    galera.append(dados[:])
    dados.clear()

    qc = str(input('Deseja continuar? ')).upper().strip()[0]

    while qc not in 'SN':
        qc = str(input('Resposda ínvalida!\nDigite "S" para Sim ou "N" para Não.\nDeseja continuar? ')
                 ).upper().strip()[0]
    if qc == 'N':
        break

print('\n')
print(f'N°{"":^5}|{"NOME":^25}|{"":<5}{"MÉDIA":<5}')
for p, aluno in enumerate(galera):
    print(f'{p} {"":^5}|{aluno[0]:<25}|{"":^5}{((aluno[1] + aluno[2] + aluno[3] + aluno[4]) / 4):^5.2f}')
print('-=-'*30)
while True:
    m = int(input('Mostrar notas de qual aluno? (999 para finalizar programa.) '))
    if m == 999:
        print('PROGRAMA FINALIZADO')
        break
    else:
        print(f'As notas de {galera[m][0]} são {galera[m][1:]}')
