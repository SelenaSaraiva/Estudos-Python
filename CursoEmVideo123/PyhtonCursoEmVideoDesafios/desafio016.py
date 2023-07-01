# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math

num  = float(input('Informe um número real: '))
ardb = math.floor(num)
ardc = math.ceil(num)
print('O arredondamento para baixo de {} é igual a: {} \n O arredondamento para cima de {} é igual a: {}'.format(num, ardb, num, ardc))

print('--------------------------------------------------------------------------------------------------------------')

# 2° forma

import math

num = float(input('Informe um número real: '))
print('A porção inteira de {} é igual a: {}'.format(num, math.trunc(num)))


print('--------------------------------------------------------------------------------------------------------------')


# 3° forma

from math import trunc

num = float(input('Informe um número real: '))
print('A porção inteira de {} é igual a: {}'.format(num, trunc(num)))


print('--------------------------------------------------------------------------------------------------------------')


# 4° forma

num = float(int('Informe um número: '))
print('A porção inteira de {} é igual a : {}'.format(num, int(num)))