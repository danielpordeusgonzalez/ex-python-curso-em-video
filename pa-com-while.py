primeiro = int(input('qual sera seu primeiro termo: '))
r = int(input('digite a razão de sua pa: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} > '.format(termo), end='')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('\n voce quer mostrar mais quantos termos ? se quiser sair do programa digite 0: '))
print('progressão finalizada com {} termos sendo utilizadas'.format(total))
