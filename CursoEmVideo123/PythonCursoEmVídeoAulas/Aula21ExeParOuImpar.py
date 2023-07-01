def par(n=3): 
    if n % 2 == 0:
        return True
    else: 
        return False 


num = int(input('Informe um valor: '))

# Segunda opção para mostrar informação; 
if par(num): 
    print('É PAR!')
else: 
    print('É ÍMPAR!')