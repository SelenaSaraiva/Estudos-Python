# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e
# os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

# Definindo listas;
listaGeral = []
listaPares = []
listaImpar = []


# Declarações e variáveis;
c = 1

# Funcionamento;
while True:

    # Entrada de valor pelo usuário;
    listaGeral.append(int(input(f'Informe o \033[4;33m{c}°\033[m valor:  ')))
    c += 1

    # Perguntando ao usuário se deseja continuar;
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [\033[4;32mS\033[m/\033[4;31mN\033[m]? ')).strip().upper()[0]
    print('\033[33m-=-\033[m'*10)

    # Comando de parada caso não deseje continuar;
    if continuar == 'N':
        break

# Caso seja par;
for i, v in enumerate(listaGeral):
    if v % 2 == 0:
        listaPares.append(v)

    # Caso seja ímpar;
    elif v % 2 == 1:
        listaImpar.append(v)

# Informações finais;
print(f'\033[4;36mTODOS\033[m \033[4mOS VALORES INSERIDOS\033[m \n\033[33m{listaGeral}\033[m')
print()

print(f'\033[4mNÚMEROS\033[m \033[4;36mPARES\033[m \n\033[33m{listaPares}\033[m')
print()

print(f'\033[4mVALORES\033[m \033[4;36mÍMPARES\033[m \n\033[33m{listaImpar}\033[m')