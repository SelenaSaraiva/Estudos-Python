# Ajuda interativa; 
# print(input.__doc__)

# Docstrings; 
def contador(i, f, p):
    """ 
    -> FAZ A SOMA DE TRÊS VALORES E MOSTRA O RESULTADO NA TELA; 
    :PARAM i: início da contagem 
    :PARAM f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
     """ 
    c = i
    while c <= f: 
        print(f'{c}', end='..')
        c += p
    print('FIM!')

# Caso de ajuda; 
# print(contador.__doc__); 

# Programa principal; 
contador(0, 10, 2)


