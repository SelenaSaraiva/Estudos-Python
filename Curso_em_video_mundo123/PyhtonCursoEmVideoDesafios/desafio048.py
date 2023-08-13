#Faça um programa que calcule a soma entre
#todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

from time import sleep
contN = 0
s = 0

print('\033[34mIniciando a soma dos ímpares múltiplos de 3 de 1 até 500 ...\033[m')
print('\033[34m-=-\033[m'*20)
sleep(2)

for c in range(1, 501, 2):
    if c % 3 == 0:
        s = s + c #ou s+=c
        contN = contN + 1 #ou contN +=1
        print(c)
print('\033[34m-=-\033[m'*20)
print('A soma dos {} números ímpares múltiplos de 3 presentes entre 1 até 500, é igual a: \033[4;34m{}\033[m'.format(contN, s))