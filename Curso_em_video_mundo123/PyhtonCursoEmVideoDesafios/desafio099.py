# Faça um programa que tenha uma função chamada maior(),
# que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

# Bibliotecas;
from time import sleep

# Apresentações; 
print('     \033[91m----------------\033[m')
print('     \033[91mANÁLISE NUMÉRICA\033[m')
print('     \033[91m----------------\033[m')

# Def; 
def maior(* num):

     # Quantidade de valores informados;
    print(f'Foram informados \033[4;33m{len(num)}\033[m valor(es)')
    
    # Mostrand cada valor, com pausa, na tela; 
    for v in num:
        print(f'{v}', end=' ', flush=True)
        sleep(0.5)
    
    # Mostrando maior valor; 
    print(f'\nMAIOR VALOR: \033[4;33m{max(num)}\033[m')
    print()
    


# Programa principal; 
maior(2, 6, 4, 8, 5)
maior(5, 1, 0, 9)
maior(10, 5, 7)
maior(12, 9)
maior(0)

