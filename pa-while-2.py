p1 = int(input('digite o primeiro termo: '))
r = int(input('digite a razão de sua pa: '))
termo = p1
total = 0
c = 1
mais = 10

while mais != 0:
    total += mais
    while c <= total:
        print('{} > '.format(termo), end='')
        termo += r
        c += 1
    print('PAUSA')
    mais = int(input('\n voce quer mostrar mais quantos termos ? se quiser sair do programa digite 0: '))
print('progressão finalizada com {} termos sendo utilizadas'.format(total))


