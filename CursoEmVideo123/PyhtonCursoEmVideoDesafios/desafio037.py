print('                     Conversor numérico                   ')
print('-=-'*20)

num = int(input('Digite um número: '))

print('[1] Binário')
print('[2] Octal ')
print('[3] Hexadecimal')

opcaoN = str(input('Escolha uma das opções de conversão acima: '))

print('-=-'*20)

if opcaoN == '1':
    b = str(bin(num))
    print('O número {} convertido em binário: {}'.format(num, b[2:]))
elif opcaoN == '2':
    o = str(oct(num))
    print('O número {} convertido em octal: {}'.format(num, o[2:]))
elif opcaoN == '3':
    h = str(hex(num))
    print('O número {} convertido em hexadecimal: {}'.format(num, h[2:]))
else:
    print('Opção inválida! Tente novamente.')
