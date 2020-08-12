import random
n1 = str(input('Primeiro aluno(a): '))
n2 = str(input('Segundo aluno(a): '))
n3 = str(input('Terceiro aluno(a): '))
n4 = str(input('Quarto aluno(a): '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação é de \n{}'. format(lista))
