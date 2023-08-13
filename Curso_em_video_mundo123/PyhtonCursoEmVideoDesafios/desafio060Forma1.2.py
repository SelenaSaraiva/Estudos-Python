# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo:5! = 5 x 4 x 3 x 2 x 1 = 120

from time import sleep

# Apresentações; (opcional)
print('                    \033[36mFATORIANDO\033[m                   ')
print('\033[36m-=-\033[m' * 20)
sleep(2)

# Entrada de valor a ser fatorido;
num = int(input('Digite o número que deseja fatoriar: '))
cont = num

# Atribuindo um valor inicial a fato;
fato = 1

# Tratando resposta;
while cont > 1:
    fato = fato * cont
    cont = cont - 1

print('\033[36m-=-\033[m' * 20)
print('{}! = \033[4;31m{}\033[m '.format(num, fato))