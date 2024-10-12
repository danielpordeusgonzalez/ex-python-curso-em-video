sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('dado invalido, informe seu sexo novamente: ')).strip().upper()[0]
print('sexo {} registrado com sucesso'.format(sexo))
