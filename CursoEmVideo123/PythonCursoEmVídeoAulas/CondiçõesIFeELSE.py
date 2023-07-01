# 1° teste

print('1° teste ------------------------------------------------------------')

nome = str(input('Qual o seu nome? '))
if nome == 'Selena':
    print('Que nome lindo você tem!')
else:
    print('O seu nome é muito popular. ')
print('Bom dia, {}!'.format(nome))

print('2° teste ------------------------------------------------------------')

# 2° teste

n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))

media = (n1 + n2)/2

print('A sua média foi {:.1f}'.format(media))

if media >= 6:
    print('Parabéns, você foi aprovado! ')
else:
    print('Infelizmente você está de recuperação!')

print('3° teste - condição simplificada ------------------------------------')

n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))

media = (n1 + n2)/2

print('A sua média foi {:.1f}'. format(media))
print('Aprovado.Parabéns!' if media >= 6 else 'Recuperação!')
