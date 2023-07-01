# Faça um programa que leia nome e média de um aluno, guardando também a situação
# em um dicionário. No final, mostre o conteúdo da estrutura na tela.

# Definindo dicionário;
boletim = {}

# Apresentações;
print('\033[36m    Cadastro do boletim\033[m')
print('\033[36m-=\033[m'*15)


# Entrada de nome e média do aluno;
boletim['Nome'] = str(input('Nome do aluno: ')).strip().upper()
boletim['Média'] = float(input('Média do aluno: '))


# Verificando média do aluno (APROVADO OU REPROVADO);
if boletim['Média'] >= 7:
    boletim['Situação'] = '\033[4;32mAPROVADO(A)\033[m'

elif 5 <= boletim['Média'] < 7: 
    boletim['Situação'] = '\033[4;33mRECUPERAÇÃO\033[m'

else: 
    if boletim['Média'] < 5: 
        boletim['Situação'] = '\033[4;31mREPROVADO\033[m'

# Mostrando conteúdo final;
print()
print('\033[36m-=\033[m'*15)
print('\033[36m          BOLETIM\033[m')
print('\033[36m-=\033[m'*15)

for k, v in boletim.items():
    print(f'{k}: \033[33m{v}\033[m')
print('\033[36m-=\033[m'*15)