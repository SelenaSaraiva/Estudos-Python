# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

nome = input('Informe o nome do funcionário: ')
sal = float(input('Informe o salário do funcionário: '))
aum = float(input('Informe a % do aumento: %'))

c = (sal * aum)/100
salAtuali = sal + c

print('O salário de {} no valor de R${:.2f} sofreu um aumento de {}%, seu novo salário é igual a: R${:.2f} '.format(nome, sal, aum, salAtuali))