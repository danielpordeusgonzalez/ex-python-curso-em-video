largura = float(input('qual a largura da sua parede em metros: '))
altura = float(input('qual a altura da sua parede em metros: '))
area = largura * altura
quantidadeTinta = area / 2

print('a largura da sua parede é {}m, a altura da sua parede é {}m, a area total da sua parede é {:.3f}m2, e  vai precisar de {:.3f}L de tinta para pinta-lá'.format(largura, altura, area, quantidadeTinta))