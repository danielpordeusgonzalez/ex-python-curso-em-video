frase = str(input('digite uma frase: ')).strip()

qntApareceu = frase.upper().count('A')

primeiraVezApareceu = (frase.upper().find('A') + 1)

ultimaVezApareceu = (frase.upper().rfind('A') + 1)

print('a letra A apareceu {} e a primeira vez que apareceu foi na posição {}, e a ultima vez que ela apareceu foi {}'.format(qntApareceu, primeiraVezApareceu,ultimaVezApareceu))