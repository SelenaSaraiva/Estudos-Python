# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

# Definindo lista;
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Atribuições e variáveis;
contPar = 0

# Entrada de valores para cada posição;
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Informe um valor para [{l}, {c}]: '))

        # Somando os valores pares;
        if matriz[l][c] % 2 == 0:
            contPar += matriz[l][c]


print('\033[36m-=\033[m'*17)

# Visualização final da matriz;
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print('\033[36m-=\033[m'*17)


# Mostrando ao usuário a soma dos pares;
print()
print(f'A \033[33msoma\033[m de todos os \033[33mpares\033[m é igual a: \033[4;36m{contPar}\033[m')

# Somando terceira coluna e mostrando ao usuário;
soma3 = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A \033[33msoma\033[m da \033[33mterceira coluna\033[m é igual a: \033[4;36m{soma3}\033[m')

# Mostrando maior valor da segunda linha;
print(f'O \033[33mmaior\033[m valor da \033[33msegunda linha\033[m é o número: \033[4;36m{max(matriz[1])}\033[m')