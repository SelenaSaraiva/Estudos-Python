# Desenvolva um programa que leia quatro valores pelo
# teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

# Bibliotecas;
from time import sleep

# Declarações e variáveis;
cont9 = 0

# Guia;
print('\033[34mA seguir, informe 4 valores inteiros\033[m')
sleep(2)

# Entrada de valores do usuário;
numeros = (int(input('1° valor: ')),
           int(input('2° valor: ')),
           int(input('3° valor: ')),
           int(input('4° valor: ')))

print(' ')

# Contando o número 9;
print(f'O número 9 apareceu \033[4;33m{numeros.count(9)}\033[m vez(es)')

# Posição primeiro valor 3;
if 3 in numeros:
    print(f'O número 3 foi digitado na posição \033[4;33m{numeros.index(3) + 1}°\033[m')
else:
    print('O número 3 não foi digitado!')

# numeros pares;
print('Números pares informados: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(f'\033[33m{n}\033[m', end=' ')