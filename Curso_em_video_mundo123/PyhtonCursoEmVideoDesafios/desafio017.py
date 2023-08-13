# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.


import math

a = float(input('Infome o comprimento do cateto adjacente: '))
b = float(input('Informe o comprimento do cateto oposto: '))

hp = math.hypot(a, b)

print('Com base nas suas informações, o comprimento da hipotenusa é igual a: {:.2f}'.format(hp))

print('----------------------------------------------------------------------------------------------------')

# 2° forma

co = float(input('Infome o comprimento do cateto adjacente:'))
ca = float(input('Informe o comprimento do cateto oposto: '))
hi = (co  ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa é igual a: {:.2f}'.format(hi))
