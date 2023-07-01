# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação 
# de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.


# Def; 
def leiaInt(v):

    # While; 
    while True:

        # Analisando de v é inteiro(Try); 
        try:
            n = int(input(v))
        
        # Caso não seja do tipo inteiro(Except); 
        except (ValueError, TypeError): 
            print('\033[31mERRO! POR FAVOR, INFORME UM NÚMERO VÁLIDO!\033[m')
            continue
        
        # Caso esteja correto;  
        else:
            return n

# Programa principal;   
intei = leiaInt('Informe um número inteiro: ')
print(f'Número inteiro informado: {intei}')

print('\033[36m----------------------------------------------------\033[m')



# Def; 
def leiaFloat(v): 

    # While;
    while True: 
        
        # Analisando se v é real(Try); 
        try: 
            n = float(input(v))
        
        # Caso não seja do tipo float(except); 
        except(ValueError, TypeError):
            print('\033[31mERRO! POR FAVOR, INFORME UM NÚMERO VÁLIDO!\033[m')

        # Caso esteja correto; 
        else: 
            return n 

# Programa Principal; 
real = leiaFloat('Informe um número real: ')
print(f'Número real informado: {real}')



    