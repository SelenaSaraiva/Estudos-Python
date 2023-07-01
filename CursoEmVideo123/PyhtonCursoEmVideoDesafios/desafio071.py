# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

# Apresentações;
print('    \033[34mCAIXA ELETRÔNICO\033[m')
print('\033[34m-=-\033[m'*10)

# Entrada de valor;
print('\033[37mNotas disponíveis para saque: R$50, R$20, R$10, R$1\033[m')
saque = int(input('Informe o valor do saque: R$'))
print(' ')

# Atribuições e variáveis;
cedula = 50
totalSaq = saque
totalced = 0

# Funcionamento;
while True:

    # Lógica de funcionamento;
    if totalSaq >= cedula:
        totalSaq -= cedula
        totalced += 1
    else:
        if totalced > 0:
            # Visualização final
            print(f'\033[4;33m{totalced}\033[m cédulas de \033[4;32mR${cedula}\033[m')

        # Caso seja 50 e passe para 20;
        if cedula == 50:
            cedula = 20

        # Caso seja 20 e passe para 10;
        elif cedula == 20:
            cedula = 10

        # Caso seja 10 e passe para 1;
        elif cedula == 10:
            cedula = 1

        # A cada mudança de cédula, ele volta a 0 para uma nova contagem;
        totalced = 0

        # Comando de parada;
        if totalSaq == 0:
            break






