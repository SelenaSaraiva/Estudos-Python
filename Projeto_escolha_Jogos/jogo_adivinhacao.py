# Importando funções; 
from time import sleep
import random

#Função jogo da adivinhação; 
def jogar():

    # Mensagem de boas vindas ao usuário; 
    print('\033[35m*\033[m' * 40)
    print('Bem vindo ao jogo de adivinhação!')

    print('Está pronto? Vamos lá!')
    print('\033[35m*\033[m' * 45) 
    sleep(2)



    # gerando número para adivinhação; 
    numero_secreto = random.randrange(1, 101)

    # Tentativas; 
    total_de_tentativas = 0

    # Total de pontos iniciais; 
    pontos = 1000



    # Usuário definindo nível de dificuldade; 
    nivel = int(input(
    '''Informe o nível de dificuldade 
    (1) Fácil 
    (2) Médio 
    (3) Difícil
    Resposta: '''))
    print('\033[35m-\033[m' * 30 )

    # Condições: verificando e atribuindo nível de dificuldade e tentativas; 
    if (nivel == 1):
        total_de_tentativas = 20

    elif (nivel == 2): 
        total_de_tentativas = 10

    else: 
        total_de_tentativas = 5




    # Laço de repetição; 
    for rodada in range (1, total_de_tentativas + 1):

        print(f'{rodada}° tentativa ')

        # Entrada do valor pelo usuário;
        chute_str = input('Digite um número de 1 a 100: ')
        print(f'O número digitado foi: {chute_str}')
        
        # Convertendo chute_str em um número inteiro; 
        chute = int(chute_str)

        # Verificando se entrada do usuário está entre 1 e 100; 
        if (chute < 1 or chute > 100): 
            print('Digite um número entre 1 e 100')
            print('\033[35m-\033[m' * 30 )
            continue

        # Declaração de acerto, maior, menor (variáveis); 
        acertou = chute == numero_secreto
        menor = chute < numero_secreto
        maior = chute > numero_secreto

        # Condições de validação; 
        if (acertou): 
            print('Você acertou! \033[31m<3\033[m')
            print(f'Você fez {pontos} pontos! ')
            break

        else: 
            if (menor): 
                print('Você chutou um número menor que o esperado')
                print('\033[35m-\033[m' * 30 )
            
            elif (maior): 
                print('Você chutou um número maior que o esperado')
                print('\033[35m-\033[m' * 30 )

        # Calculando pontuação; 
        pontos_perdidos = abs(numero_secreto - chute)
        pontos -= pontos_perdidos

        # Somando variável 'total_de_tentativas' até 3; 
        total_de_tentativas += 1; 

    print(f'Sua pontuação final foi: {pontos}')
    print(f'NÚMERO SORTEADO: {numero_secreto}')
    print('\033[33mFim do jogo!\033[m')

if (__name__ == '__main__'): 
    jogar()
