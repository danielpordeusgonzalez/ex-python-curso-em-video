nomeCompleto = input('digite seu nome completo: ').strip()

nomeMaiusculo = nomeCompleto.upper()

print('Seu nome com todas as letras maiusculas ficou {}'.format(nomeMaiusculo))

nomeMinusculo = nomeCompleto.lower()

print('seu nome com todas as letras minusculas ficou: {}'.format(nomeMinusculo))

quantidadeLetras = len(nomeCompleto) - nomeCompleto.count(' ')

print('seu nome tem {} letras'.format(quantidadeLetras))

primeiroNome = nomeCompleto.split()

countNome = len(primeiroNome[0])

print('seu primeiro nome é {} e tem {} letras'.format(primeiroNome[0], countNome))
