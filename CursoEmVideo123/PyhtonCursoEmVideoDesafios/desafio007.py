# Leia as notas de um aluno e mostre sua média

print('                  *----------------Média escolar----------------*            ')

nome = str(input('Informe o nome completo do aluno: '))
sala = str(input('Informe a sala do aluno: '))
periodo = str(input('informe o período do aluno: '))

print('------------------------------------------------------------')

n1 = int(input('Informe a primeira nota: '))

n2 = int(input('Informe a segunda nota: '))

n3 = int(input('Informe a terceira nota: '))

n4 = int(input('Informe a quarta nota: '))

media = (n1 + n2 + n3 + n4)/4

print('------------------------------------------------------------')

print(' Aluno:{} \n Sala:{} \n Período:{} \n Média:{}'.format(nome, sala, periodo, media))
