# Crie um programa onde o usuário possa digitar sete valores numéricos e
# cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
# No final, mostre os valores pares e ímpares em ordem crescente.

# Adicionando listas;
numeros = [[], []]
info = []

# Entrada de 7 valores pelo usuário;
for c in range(0,7):
    info.append(int(input(f'Insira o \033[4;33m{c + 1}°\033[m valor: ')))

# Separando os números pares e ímpares;
for v in info:

    # Caso seja par;
    if v % 2 == 0:
        numeros[0].append(v)

    # Caso seja ímpar;
    else:
        if v % 2 == 1:
            numeros[1].append(v)

print('\033[33m-=-\033[m'*10)

# Mostrando números pares;
print(f'Números \033[4;33mPARES\033[m informados: \033[36m{sorted(numeros[0])}\033[m')

# Mostrando números ímpares;
print(f'Numeros \033[4;33mÍMPARES\033[m informados: \033[36m{sorted(numeros[1])}\033[m')