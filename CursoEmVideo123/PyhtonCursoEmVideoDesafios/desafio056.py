# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é
# o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

somaMedia = 0
mediaIdade = 0
contM = 0
nomeHomem = ' '
idadeHomem = 0

# -------------------------------------------------
for c in range(1, 5):

    # Entrada de informações do usuário;
    print('{}° PESSOA'.format(c))
    nome = str(input('Digite seu nome: ')).upper()
    idade = int(input('Informe sua idade: '))
    sexo = str(input('Informe o seu sexo (\033[4;31mF\033[m ou \033[4;34mM\033[m): ')).upper()
    print('\033[93m-=-\033[m' * 20)

    # Calculando a soma da media de idade do grupo;
    somaMedia = somaMedia + idade

    # Descobrindo homem mais velho;
    if sexo == 'M':
        if idade > idadeHomem:
            idadeHomem = idade
            nomeHomem = nome

    # Descobrindo quantas mulheres tem menos de 20 anos;
    if sexo == 'F':
        if idade < 20:
            contM = contM + 1

# calculando a média de idade;
mediaIdade = somaMedia / 4
# -------------------------------------------------

print('- Média de idade do grupo: \033[4;33m{}\033[m'.format(mediaIdade))
print('\033[91m-*\033[m' * 15)

print('- \033[4;93mHomem mais velho\033[m \nNome: {} \nIdade: {} anos'.format(nomeHomem, idadeHomem))
print('\033[91m-*\033[m' * 15)

print('- Quantidade de mulheres com menos de 20 anos: \033[4;33m{} MULHER(ES)\033[m'.format(contM))