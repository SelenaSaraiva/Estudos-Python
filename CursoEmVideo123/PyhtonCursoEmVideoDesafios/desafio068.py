# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
# quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

# Bibliotecas;
import random
from time import sleep

# Apresentações;
print('        \033[4;31mPAR\033[m OU \033[4;34mIMPAR\033[m?      ')
print('\033[93m-=-\033[m' * 10)

# Inserindo nome;
nome = str(input('Digite seu nome: ')).upper()

# Boas vindas;
print(f'Olá, \033[36m{nome}!\033[m Vamos começar? Escolha sua opção a seguir e boa sorte! ')
sleep(2)
print('\033[93m-=-\033[m' * 10)

# Atribuições e variáveis;
maquina = ' '
contV = 0
c = 1

# Tratando jogo;
while True:

    # Jogada PAR OU ÍMPAR do usuário;
    Usua = str(input(f'\033[33m{c}°\033[m\033[4mPAR\033[m \033[31m(P)\033[m ou \033[4mÍMPAR\033[m \033[34m(I)\033[m:')).upper()

    # Jogada de maquina;
    if Usua == 'P':
        maquina = 'I'

    elif Usua == 'I':
        maquina = 'P'

    # Jogada numérica do usuário;
    print('Agora digite um número de \033[4;36m1\033[m a \033[4;36m10\033[m')
    numUsua = int(input('Número: '))

    # Jogada numérica de máquina;
    numMaquina = random.randint(1, 10)

    # Descobrindo ÍMPAR ou PAR;
    soma = numUsua + numMaquina

    # Caso seja PAR;
    if soma % 2 == 0:
        if Usua == 'P':
            print(f'\033[4;32m{nome}\033[m FOI O(A) \033[4;32mVENCEDOR(A)!\033[m')
            contV += 1
            c += 1

        elif maquina == 'P':
            print(f'Jogada de máquina: {numMaquina}')
            print(f'\033[4;33mTOTAL: {soma}\033[m')
            print('\033[91m-\033[m' * 35)
            print('\033[4;32mMÁQUINA VENCEU!\033[m \n\033[33mMAIS SORTE DA PRÓXIMA VEZ ...\033[m')
            break
        print(f'Jogada de máquina: {numMaquina}')
        print(f'\033[4;33mTOTAL: {soma}\033[m')
        print('\033[93m-=-\033[m' * 10)

    # Caso seja ÍMPAR;
    elif soma % 2 == 1:
        if Usua == 'I':
            print(f'\033[4;32m{nome}\033[m FOI O(A) \033[4;32mVENCEDOR(A)!\033[m')
            contV += 1
            c += 1

        elif maquina == 'I':
            print(f'Jogada de máquina: {numMaquina}')
            print(f'\033[4;33mTOTAL: {soma}\033[m')
            print('\033[91m-\033[m' * 35)
            print('\033[4;32mMÁQUINA VENCEU!\033[m \n\033[33mMAIS SORTE DA PRÓXIMA VEZ ...\033[m')
            break
        print(f'Jogada de máquina: {numMaquina}')
        print(f'\033[4;33mTOTAL: {soma}\033[m')
        print('\033[93m-=-\033[m' * 15)

# Apresentações finais;
print(f'Vitórias consecutivas de \033[4;36m{nome}\033[m: \033[4m{contV}\033[m')
print('\033[91m-\033[m' * 35)









