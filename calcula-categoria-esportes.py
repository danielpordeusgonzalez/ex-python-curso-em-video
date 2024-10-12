nascimento = int(input('digite o ano que voce nasceu: '))

idade = 2024 - nascimento

if idade <= 9:
    print('o atleta tem {}'.format(idade))
    print('voce é da catégoria mirim')
elif idade <= 14:
    print('o atleta tem {}'.format(idade))
    print('voce é da categoria infantil')
elif idade <= 19:
    print('o atleta tem {}'.format(idade))
    print('voce é da categoria junior')
elif idade <= 20:
    print('o atleta tem {}'.format(idade))
    print('voce é da categoria senior')
else:
    print('o atleta tem {}'.format(idade))
    print('voce é da categoria master')
