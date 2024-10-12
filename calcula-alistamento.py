nascimento = int(input('em que ano voce nasceu? '))

if 2024 - nascimento < 18:
    prazo = 2024 - nascimento
    prazoFuturo = 18 - prazo
    print('voce ainda vai se alistar e falta {} ano/s para isso acontecer'.format(prazoFuturo))
elif 2024 - nascimento == 18:
    print('está na hora de voce se alistar')
else:
    prazo = 2024 - nascimento
    prazoPassado = prazo - 18
    print('voce já passou do tempo do alistamento a {} ano/s'.format(prazoPassado))
