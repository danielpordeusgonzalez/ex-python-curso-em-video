n = int(input('digite um numero para saber se é primo: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
if tot == 2:
    print('\n é um numero primo')
else:
    print('\n não é um numero primo')

