# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show
# que será um valor lógico (opcional) indicando se será mostrado ou não 
# na tela o processo de cálculo do fatorial.


# Apresentações; 
print('\033[31m============================\033[m')
print('        \033[31mFATORIANDO\033[m')
print('\033[31m============================\033[m')


# def; 
def fatorial(num, show=False):
    ''' *calculando o fatorial de um número*
    :param num: Entrada de valor a ser fatoriado; 
    :param show: Mostrar ou não a conta completa; 
    :return: Retornará o resultado do valor fatoriado;'''

    # Calculando fatorial; 
    f = 1
    for c in range(num, 0, -1):

        # Processo de cálculo do fatorial; 
        if show: 
            print(c, end=' ')
            if c > 1: 
                print('X', end=' ')
            else: 
                print('=', end=' ') 

        f *= c
    return f


# Programa principal;
print(fatorial(6, show=True))
