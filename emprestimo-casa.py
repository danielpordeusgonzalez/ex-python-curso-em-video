homeValue = float(input('qual o valor da casa que voce quer comprar? R$'))
buyerSalary = float(input('qual o valor do seu salário? R$'))
howYears = int(input('quantos anos voce vai pretende pagar? '))

howMonths = howYears * 12

monthlyInstallment = homeValue / howMonths

maximumBenefit = buyerSalary * 0.3

print('para pagar uma casa de R${:.2f} em {} anos a prestação sera de {:.2f}'.format(homeValue, howYears, monthlyInstallment))

if monthlyInstallment <= maximumBenefit:
    print('emprestimo APROVADO')
else:
    print('emprestimo NEGADO')
