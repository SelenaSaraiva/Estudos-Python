# adicionar comentario 

# Apresentações;
print('\033[36m APROVEITAMENTO JOGADOR\033[m')

# Definindo dicionário e lista;
jogador = {}
gols = []
tabela = []

# Atribuições e varáveis;
contGols = 0
cont = 1

# Funcionamento; 
while True:

    # Entrada de informações pelo usuário (NOME E N° DE PARTIDAS);
    print()
    print('\033[36m=\033[m' * 25)
    print(f'\033[33m{cont})\033[m', end=' ')

    # Limpando dicionário; 
    jogador.clear()

    jogador['Nome'] = str(input('Nome do jogador: ')).strip().upper()
    jogador['Partidas jogadas'] = int(input('N° de partidas jogadas: '))

    # Limpando informações de lista; 
    gols.clear()

    # Entrada N° de gols em cada partida;
    print('\033[36m-\033[m'*25)
    for c in range(1, jogador['Partidas jogadas'] + 1):
        gols.append(int(input(f'N° de Gols na {c} partida: ')))

    # Passando n° de gols da lista para o dicionário e somando o total de gols;
    jogador['N° de gols'] = gols[:]
    jogador['Total de gols'] = sum(gols)

    # Jogando os dicionários na lista;
    tabela.append(jogador.copy())


    # Perguntando ao usuário se deseja continuar;
    print('\033[31m-=\033[m'*10)
    continuar = str(input('Deseja continuar: ')).strip().upper()

    # Contando sequência;
    cont += 1

    # Comando de parada caso a resposta seja n;
    if continuar == 'N':
        break
print('\033[33m*=\033[m'*15)

# Mostrando nome dos campos; 
for i in jogador.keys():
    print(f'{i:<14} ', end='')


for k, v in enumerate(tabela): 
    print(f'{k + 1}° ', end='')
    for d in v.values(): 
        print(f'{str(d):<14} ', end='')
    print()

# Análise separada dos jogadores; 
while True: 
    print('\033[31m-\033[m'*20)
    procura = int(input('Qual jogador deseja analisar(999 PARA ENCERRAR): '))
    print('\033[31m-\033[m'*20)
    
    if procura == 999: 
        break
    if procura >= len(tabela): 
        print('Jogador não encontrado!')
    else: 
        print(f'Levantamento jogador: {tabela[procura]["Nome"]}')
        for i, g in enumerate(tabela[procura]["N° de gols"]): 
            print(f'Jogo {i+ 1} fez {g} gols')