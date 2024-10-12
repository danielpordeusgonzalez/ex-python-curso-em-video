from datetime import date
atual = date.today().year
contadorMaior = 0
contadorMenor = 0
for pess in range(1, 8):
    ano = int(input('em que ano a {} pessoa nasceu? '.format(pess)))
    idade = atual - ano
    if idade >= 18:
        contadorMaior += 1
    else:
        contadorMenor += 1
print('{} são maior de idade e {} são menor de idade'.format(contadorMaior, contadorMenor))
