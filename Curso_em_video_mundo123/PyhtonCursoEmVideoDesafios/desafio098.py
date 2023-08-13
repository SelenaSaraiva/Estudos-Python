# Faça um programa que tenha uma função chamada contador(), que receba 
# três parâmetros: início, fim e passo. Seu programa tem
# que realizar três contagens através da função criada: 
#  a) de 1 até 10, de 1 em 1
# b) de 10 até 0, de 2 em 2  
# c) uma contagem personalizada

print('\033[36m=====================\033[m')
print('\033[36m      CONTAGEM\033[m')
print('\033[36m=====================\033[m')

# Bibliotecas; 
from time import sleep


# Def; 
def contador(i, f, p):

    # Caso passo seja negativo; 
    if passo < 0: 
        passo *= -1

    # Caso passo seja 0; 
    if passo == 0: 
        passo = 1


    print(f'CONTAGEM DE \033[4;33m{i}\033[m até \033[4;33m{f}\033[m de \033[4;33m{p}\033[m em \033[4;33m{p}\033[m')
    sleep(2.5)

    
    # Caso seja contagem positiva; 
    if i < f:
        c = i
        while c <= f:
            print(f'{c}', end=' ', flush=True)
            sleep(0.5)
            c += p 
        print('\n')


    # Caso seja contagem negativa; 
    else: 
        c = i
        while c >= f: 
            print(f'{c} ', end=' ', flush=True)
            sleep(0.5)
            c -= p
        print('\n')
        

# Programa principal; 
contador(1, 10, 1)
contador(10, 0, 2)


# Entrada de informações pelo usuário;
print('\n\033[4;36mPERSONALIZE SUA CONTAGEM\033[m')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

# Programa principal da contagem personalizada; 
contador(inicio, fim, passo)

