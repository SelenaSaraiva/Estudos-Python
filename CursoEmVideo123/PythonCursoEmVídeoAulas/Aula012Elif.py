nome = str(input('Informe o seu primeiro nome: '))

if nome == 'Selena':
    print('Que nome lindo você tem!')
elif nome == 'Carlos' or nome == 'Gustavo' or nome == 'Geaz':
    print('Belo nome masculino!')
elif nome in 'Paula Ana Maria Gabriela':
    print('Seu nome é muito popular no Brasil!')
else:
    print('Seu nome é normal!')
print('Prazer em te conhecer, {}{}{}!'.format('\033[4;35m', nome, '\033[m'))