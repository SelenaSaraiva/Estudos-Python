# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função
# input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. 
# Ex: n = leiaInt(‘Digite um n: ‘)


# Def; 
def leiaint(msg): 
    
    ok = False
    valor = 0

    while True: 
        n = str(input(msg))
        if n.isnumeric(): 
            valor = int(n)
            ok = True
        else: 
            print('\033[4;31mErro! Informe um valor numérico.\033[m')
        
        if ok: 
            break
    return valor 

# Programa principal;
n = leiaint('Informe um número: ')
print(f'Você digitou o valor {n}')