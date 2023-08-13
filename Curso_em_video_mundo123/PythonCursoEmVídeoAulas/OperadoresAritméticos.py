n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma  é igual a: {} \n A multiplicação  é igual a: {} \n A divisão  é igual a: {}'.format(s, m, d))
print('A divisão inteira é igual a: {} \n A exponenciação 2 é igual a: {} '.format(n1, n2, di,e))


# Outro modo de fazer: *end = ' '*

n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma  é igual a: {} A multiplicação  é igual a: {}  A divisão  é igual a: {}'.format(s, m, d), end='------')
print('A divisão inteira é igual a: {}  A exponenciação 2 é igual a: {} '.format(n1, n2, di,e))
