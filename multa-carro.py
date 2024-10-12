velocidade = int(input('qual a velocidade que o carro está? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('voce está multado! e a multa é de R${}'.format(multa))
else:
    print('voce não foi multado')