totalGasto = maisdemil = menor = cont = 0
produtoBarato = ''
while True:
    nomeProduto = str(input('digite o nome do seu produto: '))
    precoProduto = float(input('digite o preço do seu produto: '))
    cont += 1
    totalGasto += precoProduto
    if precoProduto > 1000:
        maisdemil += 1
    if cont == 1:
        menor = precoProduto
        produtoBarato = nomeProduto
    else:
        if precoProduto < menor:
            menor = precoProduto
            produtoBarato = nomeProduto
    parada = ' '
    while parada not in 'CP':
        parada = str(input('voce quer Continuar ou Parar [ C / P ]: ')).strip().upper()[0]
    if parada == 'P':
        break

print(f'o total gasto foi R${totalGasto:.2f}')
print(f'{maisdemil} compras foi/foram acima de mil reais')
print(f'é o/a {produtoBarato} mais barato')
