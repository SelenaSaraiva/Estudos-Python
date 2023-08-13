# Faça um programa que tenha uma função chamada ficha() que receba dois parâmetros opcionais
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha
# do jogador, mesmo que algum dado não tenha sido informado corretamente. 

print('\033[35m=================================\033[m')
print('\033[35m      CADASTRO DO JOGADOR\033[m')
print('\033[35m=================================\033[m')

# Def; 
def ficha(n='DESCONHECIDO', g=0):

    print(f'O jogador \033[4;33m{n}\033[m fez \033[4;33m{g}\033[m gols no campeonato!')



# Programa principal; 
nome = str(input('Informe o nome do jogador: ')).upper()
gols = str(input('Quantidade de gols: '))

if gols.isnumeric(): 
    gols = int(gols)

else: 
    gols = 0

if nome.strip() == '': 
    ficha(g=gols)
else: 
    ficha(nome, gols)