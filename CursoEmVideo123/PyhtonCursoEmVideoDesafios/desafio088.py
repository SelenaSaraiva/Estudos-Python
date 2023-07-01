# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
# para cada jogo, cadastrando tudo em uma lista composta.

# Definindo lista;
Listajogos = []
lisTemp = []

# Bibliotecas;
from time import sleep
from random import randint


# Apresentação;
print('\033[31m*-*\033[m'*15)
print('\033[32m             MEGA SENA\033[m')
print('\033[31m*-*\033[m'*15)

# Usuário informa quantidade de jogos para sorteio;
print('\033[93mA seguir, informe a quantidade de jogos que deseja sortear\033[m')
sleep(2)
quantJogos = int(input('Quantidade de jogos: '))
print('\033[31m-=-\033[m'*16)
print('\033[32m             SORTEANDO ...\033[m')
sleep(2)

# Sorteando jogos, guardando em lista e mostrando ao Usuário em ordem crescente;
for c in range(1, quantJogos + 1):
    cont = 0
    while True:
        NumJogo = randint(1, 60)
        if NumJogo not in lisTemp:
            lisTemp.append(NumJogo)
            cont += 1
        if cont >= 6:
            break
    lisTemp.sort()
    print(f'JOGO {c}: {lisTemp}')
    sleep(1)
    Listajogos.append(lisTemp[:])
    lisTemp.clear()
print('\033[31m-=-\033[m'*4, '\033[32mBOA SORTE\033[m', '\033[31m-=-\033[m'*4)