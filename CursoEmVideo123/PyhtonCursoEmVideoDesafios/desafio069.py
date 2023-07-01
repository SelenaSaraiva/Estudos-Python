# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer
# ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

# Importando bibliotecas;
from time import sleep

# Apresentações;
print('\033[34m        CADASTRO    \033[m')
print('\033[34m-=-\033[m' * 10)

print('\033[mInsira as informações solicitadas\033[m ')
print('\033[34m-=-\033[m' * 10)
print(' ')

# Atribuições e variáveis;
c = 1
mais18 = 0
quantHomens = 0
mulhermenos20 = 0

# Funcionamento;
while True:

    # Entrada de informações do usuário;
    print('\033[33m-------------------------\033[m')
    print(f'\033[4;33m{c}° PESSOA\033[m')
    idade = int(input('Informe sua idade: '))

    # Entrada de sexo já com tratamento de erro;
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe o seu sexo \033[31m[F]\033[m ou \033[34m[M]\033[m: ')).strip().upper()[0]

    # Verificando quantidade de pessoas com mais de 18;
    if idade >= 18:
        mais18 += 1

    # Verificando quantidade de homens;
    if sexo == 'M':
        quantHomens += 1

        # Verificando quantidade de mulheres com menos de 20 anos;
    if idade < 20 and sexo == 'F':
        mulhermenos20 += 1

    # Entrada de SIM ou NÃO com tratamento de erro;
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar \033[4;32mS\033[m ou \033[4;31mN\033[m? ')).strip().upper()[0]

    # Quer continuar?;
    if continuar == 'S':
        print('\033[36mCadastrando ...\033[m')
        c += 1
        sleep(2)
    else:
        if continuar == 'N':
            break

# informações finais;
print(' ')
print('\033[34m-=-\033[m' * 10)

print(f'Quantidade de pessoas cadastradas: \033[4;33m{c}\033[m')
print('\033[4;33mDentre elas, existem:\033[m')
print(f'\033[4;33m{mais18}\033[m pessoas maiores de 18 anos')
print(f'\033[4;33m{quantHomens}\033[m homem(s) cadastrado(s)')
print(f'\033[4;33m{mulhermenos20}\033[m mulhere(s) com menos de 20 anos')