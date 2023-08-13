# Escopo de variáveis; 
# def funcao(): 
    # n1 = 4
    # print(f'n1 dentro vale {n1}')


# n1 = 2
# funcao()
# print(f'n1 fora vale {n1}')

# ----------------------------

# Retornando valores; 

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s



r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(4)