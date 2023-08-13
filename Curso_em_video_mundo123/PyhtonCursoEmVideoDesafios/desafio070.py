# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

# Atribuições e variáveis;
totalCompra = 0
acimaMil = 0
c = 1
nomeBarato = ' '
precoBarato = 0


# Boas vindas;
print('       \033[36mControle de compras\033[m       ')
print('\033[36m-=-\033[m'*13)

# Instruções de uso;
print('\033[93mInsira a baixo o nome e o preço dos produtos\033[m')
print('\033[36m-=-\033[m'*13)
print(' ')

# Funcionamento;
while True:

    # Entrando com nome e preço;
    print(f'\033[36m{c}°\033[m')
    nomePro = str(input('Nome do produto: ')).strip().upper()
    valorPro = float(input('Preço do produto: R$ '))

    c += 1

    # Atribuindo nome inicialmente para uma comparação futura;
    if c == 2:
        precoBarato = valorPro
        nomeBarato = nomePro

    # Descobrindo valor total da compra;
    totalCompra += valorPro

    # Descobrindo quantos produtos custam mais de R$1000;
    if valorPro > 1000:
        acimaMil += 1

    # Descobrindo produto mais barato;
    if valorPro < precoBarato:
        precoBarato = valorPro
        nomeBarato = nomePro

    # Quer continuar? Já com tratamento de erro;
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [\033[32mS\033[m/\033[31mN\033[m]')).strip().upper()[0]
    print('\033[36m*.\033[m'*13)

    # Comando de parada;
    if continuar == 'N':
        break

# Informações finais;
print(' ')
print('\033[4;36mINFORMAÇÕES FINAIS DE SUA COMPRA\033[m')
print(f'Valor total: \033[4;33mR${totalCompra}\033[m')
print(f'Quantidade de produtos a cima de R$1000: \033[4;33m{acimaMil}\033[m')
print(f'O produto mais barato é o(a) \033[4;33m{nomeBarato}\033[m no valor de \033[4;33mR${precoBarato}\033[m')













