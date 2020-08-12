p = int(input('Qual é a porcentagem de desconto? '))
dinheiro = float(input('Qual é o preço do produto? R$ '))
des = dinheiro * ((100-p)/100)
print('O produto que custava R$ {} , com o desconto de {}% vai custar R$ {:.2f} . '.format(dinheiro, p, des))
