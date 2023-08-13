# Adicionar comentário;

# Apresentações;
print('\033[34m='*5, 'CADASTRO', '\033[34m=\033[m'*5)

# Definindo listas e dicionários;
cadastro = {}
infoPessoas = []

# Atribuições e variáveis;
contPessoas = 0
contIdade = 0

# Funcionamento; 
while True:
    cadastro.clear()
    # Entrada de nome e idade;
    cadastro['Nome'] = str(input('Nome: '))
    cadastro['Idade'] = int(input('Idade: '))

    # Somando idade para fazer a média
    contIdade += cadastro['Idade']

    # Entrada de sexo;
    while True:
        cadastro['Sexo'] = str(input('Sexo [\033[31mF\033[m/\033[34mM\033[m]: ')).strip().upper()[0]
        if cadastro['Sexo'] in 'FM':
            break

    # Copiando dicionário em lista;
    infoPessoas.append(cadastro.copy())

    # Contando quantas pessoas foram cadastradas;
    contPessoas += 1

    # Perguntando se o usuário deseja continuar;
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar [\033[32mS\033[m/\033[31mN\033[m]: ')).strip().upper()[0]
    print('\033[34m=\033[m'*20)

    # Comando de parada;
    if continuar == 'N':
        break

# Média de idade;
mediaIdade = contIdade / contPessoas

# Mostrando ao usuário;
print(f'\033[33mA\033[m) Foram cadastradas \033[33m{contPessoas}\033[m pessoas ')

print(f'\033[33mB\033[m) A média de idade das pessoas cadastradas é: \033[33m{mediaIdade:5.2f}\033[m')

print(f'\033[33mC\033[m) Mulheres cadastradas: ', end='')
for p in infoPessoas:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]} ', end=', ')
print()

print('\033[33mD\033[m) Pessoas com idade acima da média: ', end='')
for p in infoPessoas:
    if p['Idade'] >= mediaIdade:
        print(f'{p["Nome"]}')