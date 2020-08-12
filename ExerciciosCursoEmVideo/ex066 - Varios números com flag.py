soma = quant = 0
lista = []
while True:
    num = int(input('Digite um número (Digite 999 para parar): '))
    if num == 999:
        break
    else:
        soma += num
        quant += 1
        lista += [num]
print(f'''Você digitou {quant} números e a soma entre eles é {soma}.
E o maior entre eles é {max(lista)} e o menor é {min(lista)}''')
