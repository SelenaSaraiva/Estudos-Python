#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais
#alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

print('            PROGRESSÃO ARITMÉTICA              ')
print('\033[91m-=-\033[m'*20)

#Entrada de valores;
quanTermo = int(input('Quantos termos você deseja mostrar inicialmente: '))
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

cont = 1
termo = primeiro
total = 0
maisTermo = quanTermo

#Tratando resposta;
while maisTermo !=0:
    total = total + maisTermo
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo = termo + razao
        cont = cont + 1
    print('...')
    maisTermo = int(input('Quantos termos você deseja mostrar a mais: '))
print('\033[31m-=-\033[m'*20)
print('A progressão foi finalizada com {} termos!'.format(total))