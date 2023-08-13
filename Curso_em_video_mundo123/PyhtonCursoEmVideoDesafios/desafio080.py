# Crie um programa onde o usuário possa digitar cinco valores numéricos e
# cadastre-os em uma lista, já na posição correta
# de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

# Adicionando lista;
listaN = []

# Pedindo ao usuário para inserir 5 valores;
for v in range(0, 5):
    n = int(input(f'Informe o \033[4;33m{v + 1}°\033[m valor: '))

    # Definindo primeiro e/ou último valor;
    if v == 0 or n > listaN[-1]:
        listaN.append(n)

    # Fazendo comparações para valores em outras posições;
    else:
        pos = 0
        while pos < len(listaN):
            if n <= listaN[pos]:
                listaN.insert(pos, n)
                break
            pos += 1

print()
print('\033[4;32mVALORES INFORMADOS\033[m')
print(listaN)