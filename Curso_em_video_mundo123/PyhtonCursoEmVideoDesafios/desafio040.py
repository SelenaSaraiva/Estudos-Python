print("\033[35m          Calculando média final          \033[m ")
print('\033[33m-=-\033[m'*20)

nome = str(input('Digite o nome do aluno: '))

print('\033[33m-=-\033[m'*20)

n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
n3 = float(input('Informe a terceira nota: '))
n4 = float(input('Informe a quarta nota: '))

print('\033[33m-=-\033[m'*20)

media = (n1 + n2 + n3 + n4)/4

if media < 5:
    print('Infelizmente o(a) aluno(a), \033[36m{}\033[m, está \033[4;31mREPROVADO(A)!\033[m'.format(nome))
elif media == 5 or media <= 6.9:
# Ou == 5 media <= 6.9
    print('O(A) aluno(a), \033[36m{}\033[m, está de \033[4;33mRECUPERAÇÃO!\033[m'.format(nome))
elif media >= 7:
    print('O(A) aluno(a), \033[36m{}\033[m, está \033[4;32mAPROVADO!\033[m'.format(nome))
print('Sua média foi: \033[35m{}'.format(media))


