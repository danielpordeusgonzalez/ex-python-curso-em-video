n = int(input('digite um numero para saber sua fatorial: '))
c = n
f = 1
print('o fatorial de {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))