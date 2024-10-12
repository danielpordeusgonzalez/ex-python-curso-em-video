n = 0
c = 0
s = 0
n = int(input('digite algum numero: [999 para parar]: '))
while n != 999:
    c += 1
    s += n
    n = int(input('digite algum numero: [999 para parar]: '))

print('foram digitados {} numeros'.format(c))
print('a soma dos numeros foi {}'.format(s))
