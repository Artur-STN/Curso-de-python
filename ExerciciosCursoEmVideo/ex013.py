salario = float(input('Qual é o salário do Funcionário? R$ '))
p_aumento = float(input('Qual é a porcentagem do aumento? (ESCREVA SOMENTE NÚMEROS) '))
aumento = salario + (salario * (p_aumento/100))
print('Um funcionário que ganhava R$ {:.2f}, com o aumento de 15% no seu salário, irá receber R$ {:.2f} .'.format(salario, aumento))
