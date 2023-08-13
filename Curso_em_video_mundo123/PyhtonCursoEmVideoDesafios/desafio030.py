#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = int(input('Digite um número: '))

rd = num % 2

if rd == 0:
    print('O número {} é PAR! '.format(num))
else:
    print('O número {} é IMPAR!'.format(num))