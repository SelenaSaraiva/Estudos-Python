#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
#com uma pausa de 1 segundo entre eles.

from time import sleep

print('\033[31mIniciando contagem para fogos de artifício ....\033[m')
sleep(2)
print('\033[31m-=-\033[m'*20)

for c in range(10,0,-1):
    print(c)
    sleep(1)
print('\033[91m*Explosão iniciada!*\033[91m')
print('\033[31m-=-\033[m'*20)