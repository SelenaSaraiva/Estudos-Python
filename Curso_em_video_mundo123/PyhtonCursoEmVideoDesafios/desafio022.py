# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = input('Informe o seu nome completo: ')
dividido = nome.split().len()

print('Seu nome: {}'.format(nome))
print('-------------------------------------------------')

print('Em letras maiúsculas: ', nome.upper())
print('-------------------------------------------------')

print('Em letras minúsculas: ', nome.lower())
print('-------------------------------------------------')

print('Seu nome possui ao todo: ')
print('-------------------------------------------------')

print('A quantidade de letras presentes em seu primeiro nome é: {}'.format(dividido[0]))



# Segunda forma de execução

nome = input('Digite o seu nome completo: ')

div = nome.split()

print('Seu nome: {}'.format(nome))
print('-----------------------------------------')

print('O seu nome em letras maiúsculas: {}'.format (nome.upper()))
print('-----------------------------------------')

print('O seu nome em letras minúsculas:  {} '.format(nome.lower()))
print('-----------------------------------------')

print('Ao todo, o seu nome possui {} letras! '.format(len(nome) - nome.count(' ')))
print('-----------------------------------------')

print('O seu primeiro nome é {} e possui {} letras '.format(div[0], nome.find(' ')))