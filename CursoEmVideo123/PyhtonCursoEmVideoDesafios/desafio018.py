# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math

ang = float(input("Informe o ângulo: "))

c = math.cos(math.radians(ang))
s = math.sin(math.radians(ang))
t = math.tan(math.radians(ang))

print(' O cosseno do ângulo {} é igual a: {:.2f} \n O seno do ângulo {} é igual a: {:.2f} \n A tangente do ângulo {} é igual a: {:.2f} '.format(ang, c, ang, s, ang, t))
