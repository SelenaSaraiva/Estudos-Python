from random import choice

lista = []
arquivo = open('lista.txt','r+',encoding='utf-8')
while True:
    linha = arquivo.readline(100).replace('\n','')
    if linha != '':
        lista.append(linha)
    else:
        break
escolha = choice(lista)
nome = 'Selena'
print('olá ',nome,' Seu boneco escolhido hoje é: ',escolha)
print(f'Olá {nome} Seu boneco escolhido hoje é: {escolha}')
print('Olá {} Seu boneco escolhido hoje é: {}'.format(nome,escolha))


