numberOne = int(input('digite um numero: '))
numberTwo = int(input('digite outro numero: '))

if numberOne > numberTwo:
    print('o primeiro valor numero {} é maior que o segundo valor numero {}'.format(numberOne, numberTwo))
elif numberTwo > numberOne:
    print('o segundo valor numero {} é maior que o primeiro valor numero {}'.format(numberTwo, numberOne))
else:
    print('os numeros são iguais')
