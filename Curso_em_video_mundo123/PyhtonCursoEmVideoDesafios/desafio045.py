print('\033[33m                      JOKENPÔ               \033[m')
print('\033[36m-=-\033[m' * 20)

# deixando tudo pronto;
import random

lista = ('\033[4;31mPEDRA\033[m', '\033[4;32mPAPEL\033[m', '\033[4;34mTESOURA\033[m')
maquina = random.randint(0, 2)

# boas vindas e inserindo nome do usuário;
print(
    'Olá! Seja bem vindo(a)! Vamos brincar de \033[4;31mPEDRA\033[m, \033[4;32mPAPEL\033[m e \033[4;34mTESOURA\033[m? ')
nome = str(input('Insira seu nome: '))
print('Ok, bora lá! Digite sua opção, pressione \033[4;35mENTER\033[m e vamos ver quem é o vencedor .. ')
print('\033[36m-=-\033[m' * 20)

# mostrando opções e inserindo jogada do usuário;
print('''
\033[4;31m[0]PEDRA\033[m 
\033[4;32m[1]PAPEL\033[m
\033[4;34m[2]TESOURA\033[m''')
usuario = int(input('Sua jogada: '))
print('\033[36m-=-\033[m' * 20)

# animação JOKENPÔ;
from time import sleep

print('\033[33mJO\033[m')
sleep(1)
print('\033[33mkEN\033[m')
sleep(1)
print('\033[33mPÔ!\033[m')
print('\033[36m-=-\033[m' * 20)

# condições caso máquina jogue pedra;
if maquina == 0:

    if usuario == 0:  # pedra
        print('\033[4;33mEMPATE!\033[m')
        print('Jogada da máquina: {} '.format(lista[maquina]))
        print('Jogada de {}: {}'.format(nome, (lista[usuario])))

    elif usuario == 1:  # papel
        print('\033[4m{}\033[m \033[32mvenceu!\033[m'.format(nome))
        print('Jogada da máquina: {}'.format(lista[maquina]))
        print('Jogada de {}: {}'.format(nome, (lista[usuario])))

    elif usuario == 2:  # tesoura
        print('\033[4mMáquina\033[m \033[32mvenceu!\033[m')
        print('Jogada da máquina: {}'.format(lista[maquina]))
        print('Jogada de {}: {}'.format(nome, (lista[usuario])))

    else:
        print('\033[4;31mJogada INVÁLIDA!\033[m')



# condições caso  máquina jogue papel;
elif maquina == 1:

    if usuario == 0:  # pedra
        print('\033[4mMáquina\033[m \033[32mvenceu!\033[m')
        print('Jogada da máquina: {}'.format(lista[maquina]))
        print('Jogada de {}: {}'.format(nome, (lista[usuario])))

    elif usuario == 1:  # papel
        print('\033[4;33mEMPATE\033[m')
        print('Jogada da máquina: {}'.format(lista[maquina]))
        print('Jogada de {}: {}'.format(nome, (lista[usuario])))

    elif usuario == 2:  # tesoura
        print('\033[4m{}\033[m \033[32mvenceu!\033[m'.format(nome))
        print('Jogada da máquina: {}'.format(lista[maquina]))
        print('Jogada de {}: {}'.format(nome, (lista[usuario])))

    else:
        print('\033[4;31mJogada INVÁLIDA!\033[m')


# condições caso máquina jogue tesoura;
elif maquina == 2:

    if usuario == 0:  # pedra
        print('\033[4m{}\033[m \033[32mvenceu!\033[m')
        print('Jogada da máquina: {}'.format(lista[maquina]))
        print('Jogada de {}: {}'.format(nome, (lista[usuario])))

    elif usuario == 1:  # papel
        print('\033[4mMáquina\033[m \033[32mvenceu!\033[m')
        print('Jogada da máquina: {}'.format(lista[maquina]))
        print('Jogada de {}: {}'.format(nome, (lista[usuario])))

    elif usuario == 2:  # tesoura
        print('\033[4;33mEMPATE!\033[m')
        print('Jogada da máquina: {}'.format(lista[maquina]))
        print('Jogada de {}: {}'.format(nome, (lista[usuario])))

    else:
        print('\033[4;31mJogada INVÁLIDA!\033[m')