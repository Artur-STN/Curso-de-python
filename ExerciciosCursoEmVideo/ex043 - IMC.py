peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))

imc = peso / (altura**2)
print('Seu IMC é de : {:.1f}'.format(imc))
if imc <= 18.4:
    print('{}CLASSIFICAÇÃO: DESNUTRIDO{}'.format('\033[31m', '\033[m'))
elif 18.5 <= imc <= 24.9:
    print('{}CLASSIFICAÇÃO: PESO NORMAL{}'.format('\033[32m', '\033[m'))
elif 25 <= imc <= 29.9:
    print('{}CLASSIFICAÇÃO: SOBRE PESO{}'.format('\033[33m', '\033[m'))
elif 30 <= imc <= 39.9:
    print('{}CLASSIFICAÇÃO: OBESIDADE{}'.format('\033[33m', '\033[m'))
elif imc >= 40.0:
    print('{}CLASSIFICAÇÃO: OBESIDADE MÓRBIDA{}'.format('\033[31m', '\033[m'))
