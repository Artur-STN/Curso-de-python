print('-=-'*20)
print('Analisador De Triângulo')
print('-=-'*20)
ladoA = float(input('Primeiro segmento: '))
ladoB = float(input('Segundo segmento: '))
ladoC = float(input('Terceiro segmento: '))
print('-=-'*20)
soma = ladoA + ladoB

if soma > ladoC:
    print('Com os segmentos acima, é possível formar um triângulo.')
if soma < ladoC:
    print('Com os segmentos acima NÂO é possível formar um triâgulo.')
