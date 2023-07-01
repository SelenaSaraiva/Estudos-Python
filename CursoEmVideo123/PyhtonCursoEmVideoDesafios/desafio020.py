# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

print('             Ordenador de lista de sorteio            ')

print('Informe o nome dos 4 alunos que serão sortados em ordem')

n1 = input('1° aluno: ')
n2 = input('2° aluno: ')
n3 = input('3° aluno: ')
n4 = input('4° aluno: ')

lista = [n1, n2, n3, n4]

shuffle(lista)

print('-------------------------------------------------------')

print('Ordem de apresentação: ')
print(lista)