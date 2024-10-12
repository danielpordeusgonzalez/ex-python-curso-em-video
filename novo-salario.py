salario = float(input('digite seu salário atual: R$ '))

if salario > 1250:
    novoSalario = salario * 1.10
    print('seu salario era R${:.2f} e seu novo salario vai ser R${:.2f}'.format(salario, novoSalario))
else:
    novoSalario = salario * 1.15
    print('seu salario era R${:.2f} e seu novo salario vai ser R${:.2f}'.format(salario, novoSalario))
