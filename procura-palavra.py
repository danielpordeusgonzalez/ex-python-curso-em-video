cidade = input('qual o nome da sua cidade: ').strip()

s = cidade.upper().find('SANTOS')

if s == 0:
    print('existe a palavra santos e ela está no começo')
elif s > 1:
    print('existe a palavra santos mas não começa com ela')
else:
    print('não existe a palavra santos')
