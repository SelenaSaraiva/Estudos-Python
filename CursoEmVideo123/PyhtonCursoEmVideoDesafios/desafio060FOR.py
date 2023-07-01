# Desafio 60 em FOR;

# Entrada de valor;
num = int(input('Digite o número que deseja fatoriar: '))
fat = num

cont = 1

for num in range(num, 0, -1):
    cont = cont * num

print('{}! = {}'.format(fat, cont))