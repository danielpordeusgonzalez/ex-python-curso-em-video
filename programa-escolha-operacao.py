n1 = int(input('digite um valor: '))
n2 = int(input('digite um segundo valor: '))

operacao = 0
while operacao != 5:
    print(''' Agora escolha a operação que quer fazer com eles
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos numeros
    [ 5 ] sair do programa
    ''')
    operacao = int(input('qual operação voce escolheu? '))
    if operacao == 1:
        print(n1 + n2)
    elif operacao == 2:
        print(n1 * n2)
    elif operacao == 3:
        if n1 > n2:
            print('o primeiro numero é maior que o segundo')
        elif n2 > n1:
            print('o segundo numero é maior que o primeiro')
        else:
            print('os numero são iguais')
    elif operacao == 4:
        n1 = int(input('digite outro primeiro valor: '))
        n2 = int(input('digite outro segundo valor: '))

