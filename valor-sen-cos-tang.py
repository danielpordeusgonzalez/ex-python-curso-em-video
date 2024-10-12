import math

numero = float(input('digite o angulo que voce deseja: '))

print('seu seno vai ser {:.2f}, seu cosseno vai ser {:.2f} e a tangente vai ser {:.2f}'. format(math.sin(math.radians(numero)), math.cos(math.radians(numero)), math.tan(math.radians(numero))))
