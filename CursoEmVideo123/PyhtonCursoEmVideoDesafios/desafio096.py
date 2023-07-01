# Faça um programa que tenha uma função chamada área(), 
# que receba as dimensões de um terreno retangular 
# (largura e comprimento) e mostre a área do terreno.

print('\033[36m--------------------------\033[m')
print('\033[36mCALCULANDO ÁREA DO TERRENO\033[m')
print('\033[36m--------------------------\033[m')


# Entrada de valores; 
largura = float(input('Informe a largura do terreno: '))
comprimento = float(input('Informe o comprimento do terreno: '))


# Def; 
def area(l, c):
    areaT = l * c
    print('\033[33m=\033[m'*35)
    print(f'A área de um terreno \033[4;33m{l}x{c}\033[m é de: \033[4;33m{areaT}m²\033[m')


# Repassando informações; 
area(largura, comprimento)



