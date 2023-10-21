nome = input('Digite seu primeiro nome: ')

# Verificar tamanho nome; 
tamanho_nome = len(nome)

# Verificando se nome tem + de 1 letra; 
if tamanho_nome > 1:
    # Condições para o tamanho nome;
    if tamanho_nome <= 4: 
        print(f'{nome}, seu nome é curto!')

    elif tamanho_nome == 5 or tamanho_nome == 6: 
        print(f'{nome}, seu nome é normal!')

    else: 
        print(f'{nome}, seu nome é extenso!')
else: 
    print('\033[31mInforme mais de uma letra!\033[m]')