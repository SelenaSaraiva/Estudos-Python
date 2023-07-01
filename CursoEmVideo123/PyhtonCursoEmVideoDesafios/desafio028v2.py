print('                 Bem vindo(a) ao chutando certo!           ')
print('Olá! Meu nome é Ezio, sou seu amigo aqui no chutando certo. Vamos brincar de advinhar? ')
print("Vou pensar em um número inteiro de 0 a 5 e você tem que tentar adivinhar em que número pensei. Se você acertar, você ganha! Se não, eu ganho. O jogo acaba quando um de nós fizer 3 pontos. Vamos começar? ")

import random

print('---------------------------------------------------------------------------------------')

nome = input('Qual o seu nome? ')

cj1 = 0
cj2 = 0

while cj1 <= 3 or cj2 <= 3:

    print('Pensando em um número .... ')

    num = random.randint(0, 5)

    adnum = int(input('Pronto! Vamos ver se você acerta, {}. Qual o número que eu pensei? '.format(nome)))
    print('-------------------------------------------------------------------------------------')

    if adnum == num:
        cj2 = cj2 + 1
        print('Parabéns, {}! Você acertou! Um ponto para você.'.format(nome))
        print('Número pensado por Ezio: {} \nChute de {}: {}'.format(num, nome, adnum))
        print('---------------------------------------------------------------------------------')
    else:
        cj1 = cj1 + 1
        print('Eu ganhei! Mais sorte da próxima vez, {}. Um ponto para mim. '.format(nome))
        print('Número pensado por Ezio: {} \nChute de {}: {}'.format(num, nome, adnum))
        print('---------------------------------------------------------------------------------')
print('-----------------------------------------------------------------------------------------')
print('Fim de jogo! \n Pontos de Ezio: {} \n Pontos de {}: {}'.format(cj1, nome, cj2))