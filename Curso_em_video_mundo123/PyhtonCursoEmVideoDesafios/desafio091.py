# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário em Python.
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

# Definindo biblioteca;
jogadores = {}
ranking = []

# Importando bibliotecas;
from random import randint
from time import sleep
from operator import itemgetter

# Apresentações;
print('\033[31m=-\033[m'*15)
print('\033[91m      JOGANDO DADO\033[m')
print('\033[31m=-\033[m'*15)
sleep(1)

# Gerando números de 1 até 6 aleatoriamente (jogando dados);
jogadores['1° JOGADOR'] = (randint(1, 6))
jogadores['2° JOGADOR'] = (randint(1, 6))
jogadores['3° JOGADOR'] = (randint(1, 6))
jogadores['4° JOGADOR'] = (randint(1, 6))

print()

# Mostrando valores sorteados na tela;
print('\033[4;33mVALORES SORTEADOS\033[m')
for k, v in jogadores.items():
    print(f'{k}: {v}')
    sleep(1)
print()

# Ordenando dicionário e mostrando na tela;
print('\033[31m-=\033[m'*4, '\033[4;91mRANKING\033[m', '\033[31m=-\033[m'*4)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i + 1} lugar: {v[0]} com {v[1]}')
    