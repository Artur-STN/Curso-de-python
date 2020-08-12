v = float(input('Qual a velocidade atual do veiculo? '))
m = (v - 80) * 7
if v <= 80:
    print('Velocidade de {} Km/h permitida!\nContinue dirigindo com cuidado e tenha um Bom Dia!'.format(v))
else:

    print('MULTADO!\nVelocidade de {} Km/h ultrapassou o limite permitido que é de 80 Km/h.'.format(v))
    print('Por causa do seu excesso de velocidade,\nVocê pagará uma multa de R$ {:.2f}.'.format(m))
    print('Dirija com cuidado e tenha um Bom Dia!')