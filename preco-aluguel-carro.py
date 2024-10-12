diasAlugado = int(input('quantos dias esse carro foi alugado? '))
kmRodado = float(input('quantos Km rodados? '))
total = (diasAlugado * 60) + (kmRodado * 0.15)

print('O total a pagar é de R${:.2f}'.format(total))
