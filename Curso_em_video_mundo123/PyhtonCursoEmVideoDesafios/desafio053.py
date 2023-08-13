#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
#desconsiderando os espaços.
#Exemplos de palíndromos:
#APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

frase = str(input('Digite uma frase: ')).strip().upper()
print('\033[91m-=-\033[m'*20)

palavrasD = frase.split() #separar as palavras
junto = ''.join(palavrasD)#juntar todas elas sem espaço
inverso = ''

for letra in range (len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Esta frase é um \033[4;36mPOLÍNDROMO!\033[m')
    print('{} \n{}'.format(frase, inverso))
else:
    print('A frase \033[4;31mnão\033[m corresponde a um \033[4;36mPOLÍNDROMO!\033[m')