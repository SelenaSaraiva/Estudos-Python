# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores
# únicos digitados, em ordem crescente.


# Definindo lista de números;
numeros = []

# Atribuições e variáveis;
c = 1

# Funcionamento;
while True:

    # Entrada de valor pelo usuário;
    ns = (int(input(f'Informe o \033[4;33m{c}°\033[m valor: ')))

    # Adicionando número na lista caso não exista;
    if ns not in numeros:
        numeros.append(ns)
        print('\033[4;32mVALOR ADICIONADO COM SUCESSO!\033[m')
    else:
        print('\033[4;33mVALOR DUPLICADO! NÃO SERÁ ADICIONADO ...\033[m')

    # Perguntando se o usuário deseja continuar;
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [\033[4;32mS\033[m/\033[m\033[4;31mN\033[m]: ')).strip().upper()[0]

    print('\033[33m-=-\033[m' * 10)

    # Caso deseje parar;
    if continuar == 'N':
        break

    # Somando mais 1 no contador;
    c += 1

# Organização visual;
print()
print('\033[36m-=-\033[m'*8)

# Mostrando ao usuário, em ordem crescente, os valores digitados;
print('\033[4;36mVALORES INFORMADOS\033[m')
# OU: numeros.sort()
print(sorted(numeros))
print('\033[36m-=-\033[m'*8)