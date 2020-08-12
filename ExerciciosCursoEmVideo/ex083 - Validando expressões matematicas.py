expressao = input('Digite sua expressão: ')
parentessesaberto = list()
parentessesfechado = list()
for i in expressao:
    if i == '(':
        parentessesaberto.append(i)
    if i == ')':
        parentessesfechado.append(i)
if len(parentessesfechado) == len(parentessesaberto):
    print('SUA EXPRESSÃO ESTÁ CORRETA.')
else:
    print('SUA EXPRESSÃO ESTÁ ERRADA.')
