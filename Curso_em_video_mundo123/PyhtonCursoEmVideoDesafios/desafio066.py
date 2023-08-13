# Crie um programa que leia números inteiros pelo teclado. O programa
# só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre elas
# (desconsiderando o flag).

# Apresentações;
print('           \033[33mSOMATÓRIO\033[m              ')
print('\033[33m-=-\033[m' * 15)

# Informações de parada;
print('\033[31mATENÇÃO! Caso deseje pausar o programa, digite\033[m \033[4;31m999.\033[m ')
print('\033[31m-\033[m' * 50)

# Atribuições e variáveis;
c = 0
soma = 0

# Tratando resposta;
while True:
    n = int(input(f'Digite o {c}° valor: '))
    if n == 999:
        break
    c += 1
    soma += n

# Informações de saída;
print('\033[33m-=-\033[m' * 15)
print(f'Quantidade de números inseridos: \033[4;33m{c}\033[m')
print(f'A soma entre os valores digitados é igual a: \033[4;33m{soma}\033[m')