# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai
# mostrar a soma entre todos os valores pares sorteados pela função anterior.


# Bibliotecas; 
from random import randint


# Definindo lista; 
numeros = []

# ------------------------

# Def de sorteio; 
def sorteia(n): 
    numeros.append(n)

# Programa principal;
for c in range(1, 6): 
    sorteia(randint(1, 10))

print('\033[36m---------------------------------------\033[m')
print(f'Números sorteados: {numeros}')

# -------------------------


# -------------------------

# Def somar os pares;
def somaPar(num):
    contPar = 0
    for v in num:
        
        # Caso seja par; 
        if v % 2 == 0:
            contPar += v
    print(f'A \033[4;33msoma\033[m de todos os \033[4;33mpares\033[m é igual a: {contPar}')
    print('\033[36m---------------------------------------\033[m')
    

# Programa principal; 
somaPar(numeros)

# -------------------------

