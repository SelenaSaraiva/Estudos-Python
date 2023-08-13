nome = 'Selena'

cores = {'limpa': '\033[m',
         'roxo': '\033[35m',
         'amarelo': '\033[33m',
         'azul': '\033[34m'}

print('Olá! Muito prazer em te conhecer, {}{}{}!'.format(cores['roxo'], nome, cores['limpa']))