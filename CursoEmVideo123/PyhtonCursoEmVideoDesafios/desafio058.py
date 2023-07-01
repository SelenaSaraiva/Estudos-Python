print('                 Bem vindo(a) ao chutando certo! (ATUALIZADO)           ')
print('Olá! Meu nome é Ezio, sou seu amigo aqui no chutando certo. Vamos brincar de advinhar? ')
print("Vou pensar em um número inteiro de 0 a 5 e você tem que tentar adivinhar em que número pensei. Se você acertar, você ganha! ")

import random
from time import sleep
cont = 0

#Pedindo a identificação do usuário;
print('\033[93m-=-\033[m'*20)
nome = input('Qual o seu nome? ')
print('\033[93m-=-\033[m'*20)

#Iniciação de número a ser sorteado;
print('\033[4;36mVamos começar!\033[m')
sleep(1)
print('Pensando em um número .... ')
sleep(2)
num = random.randint(0,5)

#Resposta do usuário;
adnum = int(input('Pronto! Vamos ver se você acerta, {}. Qual o número que eu pensei? '.format(nome)))

#Tratando resposta;
while adnum != num:
    print('\033[4;31mRESPOSTA ERRADA!\033[m')
    adnum = int(input('Tente de novo. Qual o número que eu pensei: '))
    cont = cont + 1

#Acerto. Informações finais;
print('\033[93m-=-\033[m'*20)
print('\033[4;32mRESPOSTA CERTA!\033[m \nNúmero pensado por Ezio: \033[4;36m{}\033[m \nNúmero de tentativas: \033[4;36m{}\033[m'.format(num, cont))