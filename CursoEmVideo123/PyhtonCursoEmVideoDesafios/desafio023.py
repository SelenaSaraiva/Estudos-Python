# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados

num = int(input('Informe um número de 0 a 9999: '))

u = num // 1000 % 10
d = num // 100 % 10
c = num // 10 % 10
m = num // 1 % 10

print('Analisando o número {} ....'.format(num))
print('----------------------------------------------------')

print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))