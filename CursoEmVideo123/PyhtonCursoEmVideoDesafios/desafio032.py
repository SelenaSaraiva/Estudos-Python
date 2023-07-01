# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
print('                      Ano Bissexto!                      ')
print('-=-' * 20)

print('Quer descobrir se um ano é Bissexto? ')
ano = int(input('Informe o ano a ser analisado: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto!'.format(ano))

else:
    print('O ano {} não é Bissexto! '.format(ano))