# Parâmetros opcionais; 
# def soma(a=0, b=0, c=0): 
    # s = a + b + c
    # print(f' A soma vale: {s}')

# Programa principal; 
# soma(3, 2, 5)
# soma(5, 4)
# soma(c=2, a=7)

# --------------------------------

# Escopo de variáveis; 

def teste(): 
    x = 8 
    print(f' em teste n vale {n}')
    print(f' em teste x vale {x}')
# A variável x é local (variável local), funciona apenas em teste; 


# Programa principal; 
n = 2
print(f' em principal n vale {n}')
# print(f' em principal x vale {x}')

# A variável n é global (variável global), pois funciona em todo o código; 