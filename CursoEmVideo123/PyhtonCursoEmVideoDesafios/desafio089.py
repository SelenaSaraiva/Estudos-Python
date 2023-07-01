# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário
# possa mostrar as notas de cada aluno individualmente.

# Apresentações;
print('\033[93m*-'*5, '\033[4;93mBoletim\033[m', '\033[93m-*\033[m' * 5)

# Definindo lista;
infoAluno = []

# Atribuições e variáveis;
c = 1

# Entrada de informações;
print('\033[4;36mA SEGUIR, INSIRA AS INFORMAÇÕES, DO ALUNO, PARA REGISTRO\033[m')
print()
while True:
    print('\033[33m-=-\033[m' * 10)
    print(f'\033[4;33m{c}° ALUNO\033[m')
    nome = str(input('Nome: ')).upper()
    n1 = float(input('1° nota: '))
    n2 = float(input('2° nota: '))
    media = (n1 + n2) / 2
    infoAluno.append([nome, [n1, n2], media])
    c += 1

    # Perguntando se o usuário deseja continuar;
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja cadastrar outro aluno [\033[32mS\033[m/\033[31mN\033[m]]? ')).strip().upper()[0]

    # Comando de parada;
    if continuar == 'N':
        break

# Mostrando o boletim para o usuário;
print()
print('\033[36m-*\033[m'*15)
print(f'\033[36m{"N°":<5} {"Nome":<8} {"Média":>7}\033[m ')
print('\033[36m-*\033[m'*15)

for i, aluno in enumerate(infoAluno):
    print(f'{i:<5} {aluno[0]:<8} {aluno[2]:>6}')
print('\033[36m-*\033[m'*15)

# Mostrando as notas individualmente;
while True:
    print()
    mostrarN = int(input('Informe o \033[4;36mN°\033[m do aluno para ver suas notas(999 para interromper): '))

    # Comando de parada;
    if mostrarN == 999:
        break
    if mostrarN <= len(infoAluno):
        print(f'As notas do(a) aluno(a) \033[4;36m{infoAluno[mostrarN][0]}\033[m são \033[4;36m{infoAluno[mostrarN][1]}\033[m')

# Informação de saída;
print()
print('\033[4;32mObrigado por utilizar nossos serviços!\033[m')




