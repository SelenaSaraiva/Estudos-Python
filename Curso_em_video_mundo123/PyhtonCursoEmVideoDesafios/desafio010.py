# Exercício 010 - conversor de moedas

print('------------------ Bem vindo(a) ao conversor de moedas!------------------')

real = float(input('Informe a quantia em real que você possui: R$ '))
print('------------------------------------------------------------')
dolar = float(input('Informe o valor do dólar atualmente: U$ '))
print('------------------------------------------------------------')
euro = float(input('Informe o valor do Euro atualmente: €'))

converD = real / dolar
converE = real / euro

print('------------------------------------------------------------')

print('Com R${} você comprará: U${:.2f}'.format(real, converD))
print('Com R${} você comprará: {:.2f}€'.format(real, converE))
