contIdade = contHomens = contMulheres = 0

while True:
    idade = int(input('digite a idade da pessoa: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('digite o sexo da pessoa Feminino ou Masculino F/M: ')).strip().upper()[0]
    if idade >= 18:
        contIdade += 1
    if sexo == 'M':
        contHomens += 1
    if sexo == 'F' and idade < 20:
        contMulheres += 1
    escolha = ' '
    while escolha not in 'CP':
        escolha = str(input('quer Continuar ou Parar [ C / P ]: ')).strip().upper()[0]
    if escolha == 'P':
        break
print(f'{contIdade} pessoas são maiores de 18, {contHomens} homens foram cadastrados e {contMulheres} mulheres tem menos de 20 anos')