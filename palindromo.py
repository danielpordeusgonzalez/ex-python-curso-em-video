frase = str(input('digite uma frase: ')).strip().upper()

list = frase.split()
junto = ''.join(list)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if junto == inverso:
    print('a frase {} é um palindromo'.format(frase))
else:
    print('a frase {} não é um palindromo'.format(frase))
