#Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA,
#mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('            PROGRESSÃO ARITMÉTICA              ')
print('\033[91m-=-\033[m'*20)

#Entrada de valores;
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

cont = 1
termo = primeiro

#Tratando resposta;
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo = termo + razao
    cont = cont + 1
print('\033[4;31mFIM\033[m')