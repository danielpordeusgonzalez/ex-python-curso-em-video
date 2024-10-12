n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))

m = (n1 + n2) / 2

if m < 5:
    print('sua média foi {:.1f} e voce está reprovado'.format(m))
elif m >= 5 and m <= 6.9:
    print('sua média foi {:.1f} e voce está em recuperação'.format(m))
else:
    print('Parabéns sua media foi {:.1f} e voce foi aprovado'.format(m))
