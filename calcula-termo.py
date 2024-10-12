termo = int(input('qual será seu primeiro termo: '))
r = int(input('qual a razão da sua pa: '))
decimo = termo + (10 - 1) * r
for c in range(termo, decimo + r, r):
    print('{}'.format(c), end=' > ')
print('acabou')

