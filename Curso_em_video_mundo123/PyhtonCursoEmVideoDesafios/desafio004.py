# Leia algo pelo teclado e mostre seu tipo primitivo e suas informações;

info = input('Digite algo: ')

print('*--------Informações de {}--------*'.format(info))

print('Tipo primitivo de {}: '.format(info), type(info))
print('{} é uma informação numérica? '.format(info), info.isnumeric())
print('{} é uma informação alfanumérica? '.format(info), info.isalnum())
print('{} é uma informação alfabética? '.format(info), info.isalpha())
print('{} é uma informação escrita em letras maiúsculas? '. format(info), info.isupper())
print('{} é uma informação escrita em letras minúsculas? '.format(info), info.islower())
print('{} essa informação está capitalizada? '.format(info), info.istitle())




