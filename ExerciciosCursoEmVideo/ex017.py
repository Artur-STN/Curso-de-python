import math
co = float(input('Informe o valor do Cateto Oposto: '))
ca = float(input('Informe o valor do Cateto Adjacente: '))
hp = math.hypot(co, ca)
print('O Cateto Oposto é {}, o Cateto Adjacente é {}, e o valor da Hipotenusa é {:.2f} .'.format(co, ca, hp))
