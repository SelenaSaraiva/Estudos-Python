# Importando funções; 
from time import sleep

# Função jogo da forca;
def jogar():

    # Mensagem de boas vindas ao usuário; 
    print('\033[35m*\033[m' * 40)
    print('Bem vindo ao jogo da forca!')

    print('Está pronto? Vamos lá!')
    print('\033[35m*\033[m' * 40) 
    sleep(2)

    
    
    print('\033[33mFim do jogo!\033[m')

if (__name__ == '__main__'): 
    jogar()



