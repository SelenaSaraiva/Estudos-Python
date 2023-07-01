def leiaDinheiro(msg): 
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO!\033[m \033[4;91m{entrada}\033[m \033[31mé um preço inválido!\033[m')
        else: 
            valido = True
            return float(entrada)

