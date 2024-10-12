numero = int(input('digite um numero de 0 a 9999: '))

#n = str(numero)

#print('unidade: {}'.format(n[3]))
#print('dezena: {}'.format(n[2]))
#print('centena: {}'.format(n[1]))
#print('milhar: {}'.format(n[0]))

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print('analisando seu numero {}'.format(numero))
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))