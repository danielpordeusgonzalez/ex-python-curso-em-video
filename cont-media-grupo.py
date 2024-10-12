contIdade = 0
contIdadeHomem = []
contMulher = 0


for c in range(1, 5):
    nome = str(input('digite o nome da {} pessoa: '.format(c))).strip()
    idade = int(input('qual a idade da {} pessoa? '.format(c)))
    sexo = str(input('digite o sexo que voce se considera? da {} pessoa? H OU M '.format(c))).strip().upper()
    if sexo in 'Hh':
        contIdadeHomem = [idade, nome]
        if idade > contIdadeHomem[0]:
            contIdadeHomem = [idade, nome]
    contIdade += idade
    if sexo == 'M':
        if idade < 20:
            contMulher += 1


print('a media de do grupo é {} anos'.format(contIdade / 4))
print('o nome do homem mais velho é {}'.format(contIdadeHomem[1]))
print('a quantidade de mulheres que tem menos de 20 anos é {}'.format(contMulher))

