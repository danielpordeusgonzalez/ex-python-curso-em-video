n = c = s = menor = maior = 0
parar = 'S'
while parar not in 'Nn':
    n = int(input('digite um numero inteiro: '))
    c += 1
    s += n
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    parar = str(input('voce quer continuar? [S/N]: ')).strip().upper()[0]

print('a media dos numeros foi {}'.format(s / c))
print('o maior numero foi {}, e o menor numero foi {}'.format(maior, menor))

