#Refaça o DESAFIO 9, mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.

tab = int(input('\033[31mInsira o número da tabuada desejada: \033[m'))
print('\033[33m-=-\033[m'*20)

for c in range (0, 11):
    print('\033[33m{} x {} =\033[m \033[31m{}\033[m'.format(tab, c, (tab * c)))

