inf = dict()


def dados(*notas, s=False):
    """
     -> funcao para analisar a situacao de varios alunos.
    :arg1: notas = quantas notas voce quiser.
    :arg2: s = situacao dos alunos.
    :return: as informacoes e situacao de varios alunos.
    """
    inf['total'] = len(notas)
    inf['maior'] = max(notas)
    inf['menor'] = min(notas)
    inf['média'] = sum(notas) / inf['total']
    if not s:
        if inf['média'] >= 7:
            inf['situação'] = 'BOA'
        elif inf['média'] >= 5:
            inf['situação'] = 'RAZOÁVEL'
        else:
            inf['situação'] = 'RUIM'
    return dados


# Programa Principal
from random import randint
qv = str(input('Quer ver a situação? [S/N] ')).strip().upper()[0]
while qv not in "SN":
    qv = str(input('Resposta Ínvalida.'
                   '\nDigite "S" para Sim ou "N" para Não.\nQuer ver a situação? [S/N] ')).strip().upper()[0]
if qv == 'S':
    qv = False

dados(randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), s=qv)
# dados(9, s=False)
print(inf)
# help(dados)