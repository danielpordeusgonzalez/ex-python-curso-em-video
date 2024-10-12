import random

lista = random.randint(0,10)

count = 0

jogador = int(input('escolha um numero entre 0 a 10 e dispute contra a maquina: '))

while jogador != lista:
    count += 1
    if jogador > lista:
        jogador = int(input('é menos: '))
    elif jogador < lista:
        jogador = int(input('é mais: '))
print('o computador escolheu {} e o jogador escolheu {}'.format(lista, jogador))
print('o numero de tentativas que precisou para acertar foi/foram {}'.format(count + 1))
