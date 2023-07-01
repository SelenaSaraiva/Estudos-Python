# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

# Procurando o maior ...

maior = n1

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

print('Dentre os três números informados, o maior número é o: {}'.format(maior))

# Procurando o menor ...

menor = n1

if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

print('Dentre os três números informados, o menor número é o: {}'.format(menor))

