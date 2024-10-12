import random
print('-=-' * 20)
print('bem vindo ao jokenpo')
print('-=-' * 20)

print('estou pensando na minha jogada')
print('já pensei')

lista = ['pedra', 'papel', 'tesoura']


sortPc = random.choice(lista)

jogador = str(input('escolha entre papel, pedra e tesoura para ver se voce ganhou da maquina: '))

if (sortPc == 'pedra' and jogador == 'tesoura' or sortPc == 'tesoura' and jogador == 'papel'
        or sortPc == 'papel' and jogador == 'pedra'):
    print('voce perdeu para o computador, voce escolheu {} e ela perde para {}'.format(jogador, sortPc))
elif (jogador == 'pedra' and sortPc == 'tesoura' or jogador == 'tesoura' and sortPc == 'papel'
      or jogador == 'papel' and sortPc == 'pedra'):
    print('Parabéns, voce ganhou do computador. a sua escolha de  {} ganha do {}'.format(jogador, sortPc))
elif sortPc == jogador:
    print('voce escolheu {} e o computador escolheu {}, deu empate'.format(jogador, sortPc))
