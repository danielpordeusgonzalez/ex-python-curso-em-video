nome = str(input('digite seu nome completo: ')).strip()

nomeSeparado = nome.split()

primeiroNome = nomeSeparado[0]

print('o seu primeiro nome é {}, e o seu ultimo nome é {}'.format(primeiroNome, nomeSeparado[len(nomeSeparado)-1]))
