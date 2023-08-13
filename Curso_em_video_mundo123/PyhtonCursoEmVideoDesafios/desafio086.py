# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

# Definindo lista;
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Entrada de valores para cada posição;
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Informe um valor para [{l}, {c}]: '))

print('\033[36m-=\033[m'*30)

# Visualização final da matriz;
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()