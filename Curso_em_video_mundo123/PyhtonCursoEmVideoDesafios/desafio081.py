# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre:
# A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

# Lista números;
listaN = []

# Declarações e variáveis;
v = 1

# Funcionamento;
while True:
    # Entrada de valores pelo usuário;
    n = int(input(f'Informe o \033[4;33m{v}°\033[m número: '))
    listaN.append(n)
    v += 1

    # Perguntando ao usuário se deseja continuar;
    continuar = ' '

    while continuar not in 'SN':
        continuar = str(input('Quer continuar [\033[4;31mS\033[m/\033[32mN\033[m]:')).strip().upper()[0]
    print('\033[33m-=-\033[m'*10)

    # Comando de parada caso não deseje continuar;
    if continuar == 'N':
        break

# ----------------------------------
# Informações finais
print('    \033[4;36mINFORMAÇÕES FINAIS\033[m')
# ---------------------------------------

# Se o número 5 está na lista;
if 5 in listaN:
    print('° O número \033[4;33m5\033[m \033[4;32mestá\033[m presente na lista! ')
else:
    print('° O número \033[4;33m5\033[m \033[4;31mnão está\033[m presente na lista!')

print()

# Quantidade de números digitados;
print(f'° Foram digitados \033[4;33m{len(listaN)}\033[m valores!')

print()

# Lista em ordem decrescente;
listaN.sort(reverse=True)
print(f'° lISTA EM ORDEM DECRESCENTE \n\033[33m{listaN}\033[m')