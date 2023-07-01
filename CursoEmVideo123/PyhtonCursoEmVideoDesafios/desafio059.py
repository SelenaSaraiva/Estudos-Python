# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar[ 2 ] multiplicar[ 3 ] maior[ 4 ] novos números[ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep

opcao = '0'
maior = 0

# Boas vindas e apresentações; (opcional)
print('        \033[31mBEM VINDO(A) AO MENU MATEMÁTICO!\033[m         ')
print('\033[31m-=-\033[m' * 20)
sleep(2)

# Inserindo valores a serem trabalhados;
print('- Para começarmos, digite a seguir os dois valores a serem trabalhados')
n1 = int(input('1° valor:'))
n2 = int(input('2° valor: '))

while opcao != '5':
    # Apresentação e escolha do menu;
    print('\033[31m-\033[m' * 40)
    print('O que deseja fazer com os valores acima')
    print('''
[1] SOMAR
[2] MULTIPLICAR 
[3] MAIOR 
[4] NOVOS NÚMEROS 
[5] SAIR DO PROGRAMA ''')

    opcao = str(input('Sua opção: '))
    print('\033[31m-\033[m' * 40)

    # Tratando resposta;
    # Se opção 1;
    if opcao == '1':
        soma = n1 + n2
        print('\033[33mA soma entre {} e {} é igual a: {}\033[m'.format(n1, n2, soma))

    # Se opção 2;
    elif opcao == '2':
        multiplicar = n1 * n2
        print('\033[33mA multiplicação entre {} e {} é igual a: {}\033[m'.format(n1, n2, multiplicar))

    # Se opção 3;
    elif opcao == '3':
        if n1 > n2:
            maior = n1
        else:
            if n2 > n1:
                maior = n2
        print('\033[33mMaior valor informado: {}\033[m'.format(maior))

    # Se opcao 4;
    elif opcao == '4':
        print('Insira os novos valores')
        n1 = int(input('1° valor: '))
        n2 = int(input('2° valor: '))

print('\033[4;33mObrigado por utilizar nosso serviços!\033[m ')