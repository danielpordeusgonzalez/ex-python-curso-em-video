distancia = float(input('qual a distancia dessa viagem em km? '))

if distancia <= 200:
    passagem = distancia * 0.50
    print('o valor da sua passagem vai ser de R${}'.format(passagem))
else:
    passagem = distancia * 0.45
    print('o valor da sua passagem vai ser de R${}'.format(passagem))
