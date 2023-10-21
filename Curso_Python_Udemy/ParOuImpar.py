# Faça um programa que peça ao usuário para digitar um número inteiro,
# informe se este número é par ou ímpar. Caso o usuário não digite um número
# inteiro, informe que não é um número inteiro.


num = input('Informe um número inteiro: ')

if num.isdigit():
    numInt = int(num)

    if numInt % 2 == 0: 
        print(f'O número {numInt} é PAR!')

    else: 
        print(f'O número {numInt} é ÍMPAR!')

else: 
    print(f'O número informado não é inteiro!')

