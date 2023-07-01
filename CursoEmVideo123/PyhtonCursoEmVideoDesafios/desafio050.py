#Desenvolva um programa que leia seis números inteiros e mostre a soma
#apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

from time import sleep
soma = 0
contN = 0

print('\033[33mInsira abaixo 6 números inteiros\033[m')
print('\033[33m-=-\033[m'*20)
sleep(2)

for c in range (1, 7):
    n = int(input('{}° valor: '.format(c)))
    if n % 2 == 0:
        soma = soma + n #ou soma += n
        contN = contN + 1

print('\033[33m-=-\033[m'*20)
print('Foi informado \033[4;33m{}\033[m número(s) pare(s)! \nA soma de todos eles é igual a: \033[4;33m{}\033[m'.format(contN, soma))