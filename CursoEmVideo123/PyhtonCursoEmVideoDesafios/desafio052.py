#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

print('             É número primo?              ')
print('\033[34m-=-\033[m' * 20)

n = int(input('Digite um número: '))
print('\033[34m-=-\033[m' * 20)

contD = 0

for c in range(1, n + 1):
    if n % c == 0:
        contD = contD + 1
        print('\033[31m', end=' ')

    else:
        print('\033[93m', end=' ')

    print('{}'.format(c), end='')

print('\n\033[mO número \033[32m{}\033[m foi divisível \033[31m{}\033[m vezes '.format(n, contD))

if contD == 2:
    print('\033[32m{}\033[m é um número \033[4;32mPRIMO!\033[m'.format(n))

else:
    print('O número \033[32m{}\033[m \033[4;31mnão\033[m é \033[4;31mPRIMO!\033[m'.format(n))

