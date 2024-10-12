number = int(input('digite um numero: '))
conversion = int(input('qual conversão voce quer fazer, 1: binario, 2: octal, 3: hexadecimal: '))

if conversion == 1:
    print('{} convertido para binario é {}'.format(number,bin(number)[2:]))
elif conversion == 2:
    print('{} convertido para octal é {}'.format(number, oct(number)[2:]))
elif conversion == 3:
    print('{} convertido para hexadecimal é {}'.format(number, hex(number)[2:]))
