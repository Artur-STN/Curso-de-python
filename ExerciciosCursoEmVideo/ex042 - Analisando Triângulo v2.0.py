print('-=-'*20)
print('Analisador De Triângulo')
print('-=-'*20)
lado_a = float(input('Primeiro segmento: '))
lado_b = float(input('Segundo segmento: '))
lado_c = float(input('Terceiro segmento: '))
print('-=-'*20)

if lado_a < lado_b + lado_c and lado_b < lado_a + lado_c and lado_c < lado_a + lado_b:
    print('Com os segmentos acima, é possível formar um triângulo ', end='')
    if lado_a == lado_b == lado_c:
        print('EQUIlÁTERO.')
    elif lado_a == lado_b or lado_b == lado_c or lado_c == lado_a:
        print('ISÓSCELES.')
    elif lado_a != lado_b and lado_b != lado_c and lado_c != lado_a:
        print('ESCALENO.')
else:
    print('Com os segmentos acima NÂO é possível formar um triâgulo.')
