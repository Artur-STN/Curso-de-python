a = int(input('Primeiro Valor: '))
b = int(input('Segundo Valor: '))
c = int(input('Terceiro Valor: '))

menor = a
maior = b
# Verificando quem é menor
if b<a and b<c:
     menor = b
if c<a and c<b:
    menor = c
# Verificando quem é maior
if a>b and a>c:
    maior = a
if c>a and c>b:
    maior = c
print('O maior valor é: {}'.format(maior))
print('O menor valor é: {}'.format(menor))
