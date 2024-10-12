print('-=*20')
print('Analisador de triangulo')
print('-=*20')
l1 = int(input('digite o primeiro lado: '))
l2 = int(input('digite o segundo lado: '))
l3 = int(input('digite o terceiro lado: '))


if l2 + l3 > l1 > (l2 - l3) and l3 + l1 > l2 > (l1 - l3) and l2 + l1 > l3 > (l1 - l2):
    print('forma um triangulo')
    if l1 == l2 and l2 == l3 and l1 == l3:
        print('forma um triangulo equilátero')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('forma um triangulo isósceles')
    else:
        print('forma um triangulo escaleno')
else:
    print('não pode forma triangulo')