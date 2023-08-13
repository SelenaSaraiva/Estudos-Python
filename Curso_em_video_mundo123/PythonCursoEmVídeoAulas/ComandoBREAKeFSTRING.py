#COMANDO BREAK;
#F STRING

c = 1
soma = 0

while True:
    n = int(input(f'{c}° valor: '))

    if n == 999:
        break
    c += 1
    soma += n
print('Fim')
print(f'A soma entre os valores é igual a: {soma}')