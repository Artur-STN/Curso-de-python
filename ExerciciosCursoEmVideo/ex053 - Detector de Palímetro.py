frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
# for letra in range(len(junto)-1, -1, -1):
#     inverso += junto[letra]
print('Você digitou a frase {}.'.format(frase))
print('E o inverso dela é {}'.format(inverso))
if inverso == junto:
    print('{}Portando a frase {} ,é um palíndromo.{}'.format('\033[32m', frase, '\033[m'))
else:
    print('{}Portando a frase {} ,NÂO É um palìndromo{}'.format('\033[31m', frase, '\033[m'))
