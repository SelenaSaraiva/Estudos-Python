# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
print('                      Ano Bissexto!                      ')
print('-=-' * 20)
from datetime import date

print('Quer descobrir se um ano é Bissexto? ')
ano = int(input('Informe o ano a ser analisado ou digite 0 para saber se o ano atual é bissexto: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto!'.format(ano))

else:
    print('O ano {} não é Bissexto! '.format(ano))