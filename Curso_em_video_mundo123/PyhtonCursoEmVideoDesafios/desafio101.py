# Crie um programa que tenha uma função chamada voto() que vai receber 
# como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal
# indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


# Bibliotecas; 
from datetime import date

# Boas vindas;
print('\033[36m=====================\033[m')
print('\033[36m     VOTAÇÃO\033[m')
print('\033[36m=====================\033[m')
print()

# Def; 
def voto(anoP):
    
    # Descobrindo ano atual; 
    anoAtual = date.today().year
    
    # Descobrindo idade do usuário; 
    idade = anoAtual - anoP
    
    # Verificando voto negado; 
    if idade <= 15:
        print(f'IDADE: \033[4;33m{idade} ANOS!\033[m ')
        print('SITUAÇÃO DE VOTO: \033[4;31mVOTO NEGADO!\033[m')

    # Verificando voto opcional; 
    elif idade <= 17 or idade >= 65:
        print(f'IDADE: \033[4;33m{idade} ANOS!\033[m ')
        print('SITUAÇÃO DE VOTO: \033[4;33mOPCIONAL!\033[m')
     
    # Verificando voto obrigatório;   
    elif idade >= 18: 
        print(f'IDADE: \033[4;33m{idade} ANOS!\033[m ')
        print('SITUAÇÃO DE VOTO: \033[4;32mOBRIGATÓRIO!\033[m')



# Programa principal; 
voto(int(input('Informe seu ano de nascimento: ')))