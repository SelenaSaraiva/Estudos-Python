#Crie um programa que leia o ano de nascimento de sete pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

atual = date.today().year
totalMe = 0
totalMai = 0

for c in range (1,8):
    print('{}° - '.format(c),  end='')
    nome = str(input('Digite seu nome: '))
    anoN = int(input('Informe seu ano de nascimento: '))
    print('\033[91m-=-\033[m' * 20)

    if atual - anoN < 18:
        menor = nome
        totalMe = totalMe + 1

    elif atual - anoN >= 18:
        maior = nome
        totalMai = totalMai + 1

print('Maiores de idade \n{}'.format(maior))
print('Total de pessoas: {}'.format(totalMai))

print('Menor de idade')













