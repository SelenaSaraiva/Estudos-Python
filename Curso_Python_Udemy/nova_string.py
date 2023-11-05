nome =  'Selena Saraiva'

tamanho_nome = len(nome)

nova_string = ' ' 
c = 0
while c < tamanho_nome:
    letra = (nome[c])
    nova_string += f'*{letra}'
    c += 1
print(nova_string)



