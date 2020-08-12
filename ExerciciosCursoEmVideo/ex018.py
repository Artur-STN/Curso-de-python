import math
an = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tg = math.tan(math.radians(an))
print('O seno de {} é {:.2f}°\nO cosseno de {} é {:.2f}°\nA tangente de {} é de {:.2f}°'.format(an, seno, an, cos, an, tg))
