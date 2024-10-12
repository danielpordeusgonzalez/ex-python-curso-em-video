import random

lista = [0, 1, 2, 3, 4, 5]

numeroEscolhido = random.choice(lista)
print('estou escolhendo um numero')
print('escolhi')
numeroUsuario = int(input('escolha um numero para saber se vc acertou: '))

if numeroEscolhido == numeroUsuario:
    print('o numero da maquina foi {} e o seu numero escolhido foi {}. que isso pow vc acertou'.
          format(numeroEscolhido, numeroUsuario))
else:
    print('o numero da maquina foi {} e o seu numero escolhido foi {}. voce errou tente de novo'.
          format(numeroEscolhido, numeroUsuario))
