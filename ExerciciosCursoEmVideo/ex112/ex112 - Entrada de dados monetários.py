from ex112.utilidadesCeV import moeda
from ex112.utilidadesCeV import dado

p = dado.leiaDinheiro('Digite o preço: R$ ')
aumenta = float(input('Aumentar em quantos porcentos? '))
diminui = float(input('Diminuir em quantos porcentos? '))
moeda.resumo(p, aumenta, diminui)
