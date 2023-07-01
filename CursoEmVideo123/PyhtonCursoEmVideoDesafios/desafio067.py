# Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido
# quando o número solicitado for negativo.

# Boas vindas ao usuário;
print('                 \033[93mTABUADA\033[m                      ')
print('\033[93m-=-\033[m' * 15)

# Instruções de parada do programa;
print('\033[4;91m|ATENÇÃO! Caso deseje parar o programa, digite um número negativo. Ex: -1|\033[m')
print(' ')

# Atribuições e variáveis;
c = 0
contTab = 1

# Tratando resposta;
while True:
    print('\033[93m-\033[m' * 40)
    n = int(input(f'\033[93m{contTab}° Digite o número da tabuada desejada:\033[m  '))

    # Ordem de parada;
    if n < 0:
        break

    # Calculando e mostrando a tabuada;
    for c in range(0, 11):
        tab = n * c
        print(f'{n} x {c} = {tab} ')
        c += 1

    # Contador de tabuadas visualizadas;
    contTab += 1

# Informações de saída;
print(' ')
print('-----------------------------------------------')
print('      \033[4;31mPROGRAMA ENCERRADO!\033[m ')
print('\033[31mObrigado por utilizar nossos serviços!\033[m')
print('-----------------------------------------------')