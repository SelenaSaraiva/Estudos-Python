# Exercício 011 - Pintando parede

largura = float(input('Informe a largura da parede: '))
altura = float(input('Informe a altura da parede: '))
print('----------------------------------------------------------------------')

area = largura * altura
tinta = area/2

print('° A parede de dimensão {} x {} tem uma área de: {}mt²'.format(largura, altura, area))
print('° Litros de tinta necessário para pintar a parede atual: {}L'.format(tinta))