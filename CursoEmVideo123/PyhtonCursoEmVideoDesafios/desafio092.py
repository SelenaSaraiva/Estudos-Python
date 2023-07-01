# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

# Definindo dicionários;
cadastro = {}

# Importando bibliotecas;
from datetime import date

# Apresentações;
print('\033[33m*\033[m' * 30)
print('\033[33m   CADASTRO DO TRABALHADOR\033[m')
print('\033[33m*\033[m' * 30)

print()
print('\033[33m=-\033[m'*30)
print('Insira as seguintes informações para cadastro')
print('\033[4;91mOBS: CASO NÃO TENHA CARTEIRA DE TRABALHO, DIGITE 0.\033[m')
print('\033[33m=-\033[m'*30)

# Entrada de informações pelo usuário;
cadastro['Nome'] = str(input('Nome: ')).strip().upper()
anoNasc = int(input('Ano de nascimento: '))
cadastro['Carteira'] = int(input('Carteira de trabalho: '))

# Descobrindo ano atual e calculando idade;
ano = date.today().year
idade = ano - anoNasc
cadastro['Idade'] = idade

# Caso não tenha carteira;
print()
print('\033[33m=\033[m'*6, '\033[33mCADASTRO\033[m', '\033[33m=\033[m'*6)
if cadastro['Carteira'] == 0:
    for k, v in cadastro.items():
        print(f'{k}: {v}')
else:
    # Continuação caso possua carteira;
    cadastro['Contratação'] = int(input('Ano de contratação: '))
    cadastro['Salário R$'] = float(input('Salário R$: '))
    print('\033[33m=-\033[m' * 30)

    # Calculando idade da aposentadoria (CONSIDERANDO QUE O TEMPO DE CONTRIBUIÇÃO É 35 ANOS);
    Aposen = (cadastro['Contratação'] - anoNasc) + 35
    cadastro['Aposentadoria'] = Aposen

    # Mostrando cadastro na tela;
    print()
    print('\033[33m=\033[m'*6, '\033[33mCADASTRO\033[m', '\033[33m=\033[m'*6)
    for k, v in cadastro.items():
        print(f'{k}: {v}')