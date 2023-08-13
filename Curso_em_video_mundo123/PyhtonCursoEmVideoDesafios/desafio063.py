#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os
#N primeiros elementos de uma Sequência de Fibonacci.
#Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8


#Apresentações;
print('             \033[36mSEQUÊNCIA DE FIBONACCI\033[m              ')
print('\033[36m-=-\033[m'*20)

#Entrada de valor;
termo = int(input('Informe quantos termos deseja mostrar: '))

#Atribuições e variáveis;
t1 = 0
t2 = 1

cont = 3
soma = 0


#Termos inicias padrões;
print('{} -> {}'.format(t1, t2), end=' -> ')

#Tratando resposta;
while cont <= termo:
    t3 = t1 + t2
    print('{}'.format(t3), end=' -> ')
    t1 = t2
    t2 = t3
    cont = cont + 1