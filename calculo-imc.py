peso = float(input('qual o seu peso: (kg)'))
altura = float(input('qual a sua altura: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('voce está com {:.1f} de imc e está abaixo do peso'.format(imc))
elif 18.5 <= imc < 25:
    print(' voce está com {:.1f} de imc e está com o peso ideal'.format(imc))
elif 25 <= imc < 30:
    print('voce está com {:.1f} de imc e está com sobrePeso'.format(imc))
elif 30 <= imc < 40:
    print('voce está com {:.1f} de imc e está com obesidade'.format(imc))
elif imc >= 40:
    print('voce está com {:.1f} de imc e está com obesidade morbida'.format(imc))
