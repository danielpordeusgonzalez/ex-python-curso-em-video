valorProduto = float(input('qual o valor do produto? R$'))
print('''existe 4 opções de pagamento
[ 1 ] a vista dinheiro / cheque
[ 2 ] a vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] em até 3x ou mais no cartão
''')
opcao = int(input('qual a sua opção de método de pagamento: '))

if opcao == 1:
    valorFinal = valorProduto * 0.9
    print('o valor do produto é {} e com o desconto de 10% ficou {}'.format(valorProduto, valorFinal))
elif opcao == 2:
    valorFinal = valorProduto * 0.95
    print('o valor do produto é {} e com o desconto de 5% ficou {}'.format(valorProduto, valorFinal))
elif opcao == 3:
    print('o valor do produto é {} e continua o mesmo, sem desconto. '.format(valorProduto))
elif opcao == 4:
    valorFinal = valorProduto * 1.2
    print('o valor do produto é {} e com o juros de 20% ficou {}'.format(valorProduto, valorFinal))
else:
    print('não existe essa opção de pagamento')
