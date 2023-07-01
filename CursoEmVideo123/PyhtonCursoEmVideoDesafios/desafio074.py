# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também
# indique o menor e o maior valor que estão na tupla.

# Bibliotecas;
from random import randint

# Boas vindas;
print('\033[36m      Gerando números\033[m')
print('\033[36m-=-\033[m'*10)

print(' ')

# Gerando aleatoriamente, em uma tupla, cinco números;
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

# Apresentando números sorteados;
print('\033[4;33mOs números sorteados foram:\033[m ')
for c in numeros:
    print(f'{c} ')

print(' ')

# Descobrindo maior valor sorteado;
print(f'O \033[4;33mmaior\033[m valor sorteado foi: \033[4;33m{max(numeros)}\033[m')

# Descobrindo menor valor sorteado;
print(f'O \033[4;33mmenor\033[m valor sorteado foi: \033[4;33m{min(numeros)}\033[m')