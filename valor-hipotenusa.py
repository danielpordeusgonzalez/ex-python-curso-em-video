import math
catetoOposto = float(input('qual o cateto oposto? '))
catetoAdjacente = float(input('qual o cateto adjacente? '))

valorCatetos = (math.pow(catetoOposto,2)) + (math.pow(catetoAdjacente, 2))
hipotenusa = valorCatetos ** (1/2)

print('valor da hipotenusa é {:.2f}'.format(hipotenusa))
