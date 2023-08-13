#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

from time import sleep

print('\033[36mIniciando contagem de números pares de 1 até 50!\033[m')
print('\033[36m-=-\033[m'*20)
sleep(2)

for c in range(1, 51): #o mesmo que: for c in range(1, 51, +2)
     if c % 2 == 0:
        s = c
        print(s)

print('\033[36m-=-\033[m'*20)
print('\033[36mFim da contagem!\033[m')