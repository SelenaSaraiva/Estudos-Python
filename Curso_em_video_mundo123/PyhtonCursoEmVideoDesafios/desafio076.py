# Crie um programa que tenha uma tupla única com nomes de
# produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

# Lista de produtos e seus valores;
lista = ('Placa de Vídeo', 2.000,
         'Placa mãe', 600,
         'Mouse', 250,
         'Headset', 320,
         'MousePad', 170,
         'Teclado', 350,
         'Monitor', 1.700,
         'Gabinete', 270)

# Apresentação do nome da listagem;
print('\033[31m-=-\033[m'*13)
print('\033[91m             PC GAMER\033[m')
print('\033[31m-=-\033[m'*13)

# Mostrando e alinhando tabela;
for pos in range (0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>7.2f}')
print('\033[31m-=-\033[m'*13)