nome = input('qual seu nome: ')

s = nome.find('silva')

if s > 0:
    print('existe o nome silva e está na posição {}'.format(s))
else:
    print('nao existe silva nesse nome')
