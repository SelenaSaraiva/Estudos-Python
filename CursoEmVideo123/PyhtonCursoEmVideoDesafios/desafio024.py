#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
cid = input('Informe o nome de uma cidade: ')

div = cid.split()

print('Nome da cidade informada: {}'.format(cid))
print('A cidade citada começa com a palavra SANTO!?', div[0].find('Santo'))


# segunda forma de execução
#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cid = str(input('Informe o nome de uma cidade: ')).strip()
print(cid[:5].upper() == 'SANTO')