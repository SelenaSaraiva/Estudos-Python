# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

maiorPeso = 0
menorPeso = 0

for c in range(1, 6):
    nome = str(input('{}° Pessoa \nDigite seu nome: '.format(c)))
    peso = float(input('Informe o seu peso: '))
    print('\033[36m-=-\033[m' * 20)

    if c == 1:  # declarar um valor para inicialmente para compará-lo depois
        maiorPeso = peso
        menorPeso = peso
        nomeMaior = nome
        nomeMenor = nome

    else:
        if peso > maiorPeso:
            maiorPeso = peso
            nomeMaior = nome

        elif peso < menorPeso:
            menorPeso = peso
            nomeMenor = nome

print('\033[4;31mPessoa com maior peso\033[m \n\033[93mNome:\033[m {} \n\033[93mPeso:\033[m {}Kg '.format(nomeMaior,
                                                                                                          maiorPeso))

print('\033[4;32mPessoa com menor peso\033[m \n\033[93mNome:\033[m {} \n\033[93mPeso:\033[m {}Kg '.format(nomeMenor,
                                                                                                          menorPeso))