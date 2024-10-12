from random import randint
v = 0
while True:
    jogador = int(input('digite um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? ')).strip().upper()[0]
    print(f'vc jogou {jogador} e o computador jogou {computador}. total {total} ', end='')
    print('DEU PAR' if total % 2 == 0 else 'Deu impar')
    if tipo == 'P':
        if total % 2 == 0:
            print('parabes vc ganhou')
            v += 1
        else:
            print(' voce perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('parabes vc ganhou')
            v += 1
        else:
            print(' voce perdeu')
            break
    print('vamos jogar novamente')
print(f'game over, vc ganhou {v}')
