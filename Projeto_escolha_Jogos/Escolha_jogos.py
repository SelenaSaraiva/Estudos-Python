# Importando jogos; 
import jogo_forca
import jogo_adivinhacao


def escolhe_jogo():
    # Mensagem de boas vindas ao usuário; 
    print('\033[35m*\033[m' * 40)
    print('          ESCOLHA O SEU JOGO')
    print('\033[35m*\033[m' * 40) 

    # Apresentando escolhas para o usuário; 
    print('''(1) Forca 
    (2) Advinhação''')

    # Escolha/entrada do usuário; 
    jogo = int(input('Resposta: '))

    # Condições: entrada/atribuição de jogos; 
    if (jogo == 1):
        print('Jogando forca')
        jogo_forca.jogar()

    elif (jogo == 2): 
        print('Jogando adivinhação')
        jogo_adivinhacao.jogar()


if (__name__ == '__main__'): 
    escolhe_jogo()


