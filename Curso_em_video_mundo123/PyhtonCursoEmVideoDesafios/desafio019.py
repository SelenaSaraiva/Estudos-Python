# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.


import random

print('                    Sorteador de nomes                    ')
print('------------------------------------------------------------')

print('Insira a baixo o nome dos 4 alunos a serem sorteados')

n1 = str(input('1° aluno: '))
n2 = str(input('2° aluno: '))
n3 = str(input('3° aluno: '))
n4 = str(input('4° aluno: '))

lista = [n1, n2, n3, n4]

print('------------------------------------------------------------')

# Ou:
# sorteado = random.choice(lista)

print('O(A) sortedo(a) foi: {} '.format(random.choice(lista)))
# print('Aluno escolhido: '.format(sorteado))