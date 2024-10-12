
import random

v = 0
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('''Voce entrou no jogo par ou impar, faça sua escolha
[ P ] PAR
[ I ] IMPAR
''')
escolha = str(input('voce escolhe par ou impar [P ou I]: ')).strip().upper()[0]
while True:
    jogador = int(input('digite um numero no impar ou par e descubra se voce ganhou do computador? '))
    sortpc = random.choice(lista)
    total = sortpc + jogador
    print(f'o jogador escolheu {jogador}, o pc escolheu {sortpc} e a soma deu {total}')
    while escolha not in 'PI':
        if escolha == 'P':
            if total % 2 == 0:
                print('parabes vc ganhou')
                v += 1
            else:
                print('vc perdeu')
                break
        elif escolha == 'I':
            if total % 2 == 1:
                v += 1
                print('parabes vc ganhou')
            else:
                print('vc perdeu')
                break
    escolha = int(input('voce escolhe par ou impar [P ou I]'))
print(f'vc ganhou {v}')




