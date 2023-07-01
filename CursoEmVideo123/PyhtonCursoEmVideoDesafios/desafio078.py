#  Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#  No final, mostre qual foi o maior e o menor valor digitado e as suas
#  respectivas posições na lista.

# Declarando lista;
numeros = []

# Entrada 5 valores e adicionando na lista;
for n in range(1,6):
    n5 = int(input(f'informe o {n}° número: '))
    numeros.append(n5)

# maior e menor valor;
maior = max(numeros)
menor = min(numeros)

print('\033[33m-=-\033[m'*15)
print('\033[33m    informações finais\033[m')
print('\033[33m-=-\033[m'*15)

# Visualização de números inseridos;
print(f'Números inseridos: \033[33m{numeros}\033[m')
print(' ')

# Maior valor informado;
print(f'Maior valor informado: \033[4;33m{maior}\033[m')
print(f'Sua posição: \033[4;33m{numeros.index(maior) + 1}\033[m')
print(' ')

# Menor valor informado;
print(f'Menor valor informado: \033[4;33m{menor}\033[m')
print(f'Sua posição: \033[4;33m{numeros.index(menor) + 1}\033[m ')