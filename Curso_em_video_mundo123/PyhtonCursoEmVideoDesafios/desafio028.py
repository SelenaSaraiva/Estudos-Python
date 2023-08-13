print('                 Bem vindo(a) ao chutando certo!           ')
print('Olá! Meu nome é Ezio, sou seu amigo aqui no chutando certo. Vamos brincar de advinhar? ')
print(
    "Vou pensar em um número inteiro de 0 a 5 e você tem que tentar adivinhar em que número pensei. Se você acertar, você ganha! Vamos começar? ")
print('-=-' * 20)
import random

nome = input('Qual o seu nome? ')
print('-==' * 20)

num = random.randint(0, 5)

print('Pensando em um número .... ')

adnum = int(input('Pronto! Vamos ver se você acerta, {}. Qual o número que eu pensei? '.format(nome)))
print('-=-' * 20)

if adnum == num:
    print('Parabéns, {}! Você acertou!'.format(nome))
    print('Número pensado por Ezio: {} \nChute de {}: {}'.format(num, nome, adnum))
    print('-=-' * 20)
else:
    print('Eu ganhei! Mais sorte da próxima vez, {}. '.format(nome))
    print('Número pensado por Ezio: {} \nChute de {}: {}'.format(num, nome, adnum))
print('-=-' * 20)
print('Fim de jogo!')
