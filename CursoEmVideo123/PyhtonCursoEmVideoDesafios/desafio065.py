# Crie um programa que leia vários números inteiros pelo teclado.No final da execução, mostre a
# média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar
# ao usuário se ele quer ou não continuar a digitar valores.


# Apresentações;
print('                        \033[33mSOMATÓRIO\033[m                       ')
print('\033[33m-=-\033[m' * 20)

# Atribuições e variáveis;
resp = 'S'
c = 1
soma = 0
menor = 0
maior = 0

# Tratando resposta;
while resp == 'S':
    num = int(input('\033[36m{}°\033[m Informe um número: '.format(c)))
    resp = str(input('Deseja continuar [S/N]: ')).upper()

    # Tratando erro de escolha;
    if resp != 'S' and resp != 'N':
        resp = str(input('\033[31mOpção inválida! Digite\033[m [\033[32mS\033[m/\033[91mN\033[m]: ')).upper()

    # Atribuição inicial para tratar menor e maior valor;
    if c == 1:
        menor = num
        maior = num

    # Descobrindo maior;
    if num > maior:
        maior = num

    # Descobrindo menor;
    elif num < menor:
        menor = num
    c += 1
    soma += num
    print('\033[36m-\033[m'*35)
# Descobrindo a média;
media = soma/c

print('\033[33m-=-\033[m' * 20)
print('Foram digitados \033[4;33m{}\033[m números!'.format(c))
print('A média entre todos os valores lidos é igual a: \033[4;33m{:.2f}\033[m '.format(media))
print('Maior valor lido: \033[4;33m{}\033[m'.format(maior))
print('Menor valor lido: \033[4;33m{}\033[m'.format(menor))



