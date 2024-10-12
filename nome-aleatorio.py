import random

nome1 = input('primeiro aluno: ')
nome2 = input('segundo aluno: ')
nome3 = input('terceiro aluno: ')
nome4 = input('quarto aluno: ')

nomes = [nome1, nome2, nome3, nome4]

escolhido = random.choice(nomes)

print('o aluno escolhido foi {}'.format(escolhido))
