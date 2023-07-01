# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles

# Apresentaçõe;
print('               \033[33mSOMATÓRIO\033[m        ')
print('\033[33m-=-\033[m' * 15)

# Informações de pausa;
print('')
print('\033[4;31mATENÇÃO! CASO DESEJE PARAR O PROGRAMA, DIGITE 999.\033[m')

# Atribuições e variáveis;
# num = c = soma = 0 - atribuição simplificada
num = 0
c = 0
soma = 0

# Tratando resposta;
while num != 999:
    num = int(input('Digite um número: '))

    if num != 999:
        c = c + 1
        soma = soma + num

# Formatações;
print('\033[33m-=-\033[m' * 15)
print('Foram digitados \033[4;33m{}\033[m números'.format(c))
print('A soma entre eles é igual a: \033[4;33m{}\033[m'.format(soma))