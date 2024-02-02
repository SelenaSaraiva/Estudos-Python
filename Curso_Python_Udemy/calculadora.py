# Laço de repetição; 
while True: 

    # Entrada dos 2 valores a serem calculados; 
    n1 = float(input('Informe o 1° valor: '))
    n2 = float(input('Informe o 2° valor: '))

    # Definindo calculo; 
    print('''O que deseja fazer: 
        [1] SOMA
        [2] SUBTRAÇÃO
        [3] MULTIPLICAÇÃO
        [4] DIVISÃO''')
    calculo = int(input('Sua opção: '))

    # Caso [1] SOMA; 
    if calculo == 1:
        soma = n1 + n2 
    print(f'A soma de {n1} + {n2} = {soma}')

    # Caso [2] SUBTRAÇÃO;
    if calculo == 2: 
        subt = n1 * n2 
    print(f'A subtração de {n1} x {n2} = {subt}')
        
    #condição para sair; 
    print('-*25')
    sair = input('Deseja sair? [S]/[N]').strip().upper().startswith('S')
    if sair == 'S':
        break
