#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
#Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Informe o seu sexo [\033[4;31mF\033[m/\033[4;34mM\033[m]: ')).strip().upper()[0]
print('\033[93m-=-\033[m'*20)

while sexo not in 'MF':
    sexo = str(input('\033[4;33mOPÇÃO INVÁLIDA!\033[m \nInforme novamente o seu sexo [\033[4;31mF\033[m/\033[4;34mM\033[m]: ')).strip().upper()[0]
if sexo == 'F':
    print('Sexo \033[4;31m{}\033[m registrado com sucesso! '.format(sexo))
else:
    print('Sexo \033[4;34m{}\033[m registrado com sucesso!'.format(sexo))