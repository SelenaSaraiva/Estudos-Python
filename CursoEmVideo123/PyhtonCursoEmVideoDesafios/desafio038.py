n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo valor: '))

print('-=-'*20)

if n1 > n2:
    print('O {} número é o maior!'.format('\033[36m PRIMEIRO \033[m'))
elif n2 > n1:
    print('O {} número é o maior!'.format('\033[36m SEGUNDO \033[m'))
elif n1 == n2:
    print('Não existe valor maior, ambos são iguais!')
    

