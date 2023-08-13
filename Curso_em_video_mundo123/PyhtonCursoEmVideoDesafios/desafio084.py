# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

# Bibliotecas;
from time import sleep

# Definindo listas;
pessoas = []
info = []

# Declarações e variáveis;
maior = menor = 0


print('\033[36mInsira seu nome e peso(kg)\033[m')
print('\033[36m-=-\033[m'*10)
sleep(2)

# Entrada de nome e peso do usuário;
while True:
    info.append(str(input('Nome: ')))
    info.append(float(input('Peso(kg): ')))

    # Descobrindo menor e maior peso;
    if len(pessoas) == 0:
        maior = menor = info[1]

    else:
        if info[1] > maior:
            maior = info[1]
        if info[1] < menor:
            menor = info[1]

    # Adicionando na lista pessoas e limpando a temporária;
    pessoas.append(info[:])
    info.clear()

    # Perguntando ao usuário se deseja continuar;
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [\033[4;32mS\033[m/\033[31mN\033[m]:')).strip().upper()[0]

    print('\033[36m-=-\033[m'*10)

    # Comando de parada;
    if continuar == 'N':
        break

# Quantidade de pessoas cadastradas;
print(f'Ao todo foram cadastradas \033[4;33m{len(pessoas)}\033[m pessoas')

# Pessoas com maiores pesos;
print(f'O maior peso foi \033[4;33m{maior}kg\033[m. De ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}')

# Pessoa com menor peso;
print(f'O menor peso foi \033[4;33m{menor}\033[m', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}')





