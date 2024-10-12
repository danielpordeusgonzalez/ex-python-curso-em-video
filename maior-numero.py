n1 = int(input('digite o primeiro numero: '))
n2 = int(input('digite o segundo numero: '))
n3 = int(input('digite um terceiro numero: '))


if n1 > n2 and n1 > n3:
    print('o numero {} é maior que os outros'.format(n1))
elif n2 > n1 and n2 > n3:
    print('o numero {} é maior que os outros'.format(n2))
elif n3 > n1 and n3 > n2:
    print('o numero {} é maior que os outros'.format(n3))

if n1 < n2 and n1 < n3:
    print('o numero {} é menor que os outros'.format(n1))
elif n2 < n1 and n2 < n3:
    print('o numero {} é menor que os outros'.format(n2))
elif n3 < n1 and n3 < n2:
    print('o numero {} é menor que os outros'.format(n3))
