print('                    Empréstimo bancário!                    ')
print('-=-'*20)
print('Olá! Seja bem vindo(a)! Para começarmos a calcular seu empréstimo, precisaremos \nde algumas informações. Vamos lá?')
print('-=-'*20)

nome = str(input('Digite o seu nome: '))
vcasa = float(input('Informe o valor do imóvel: R$'))
sal = float(input('Informe o seu salário: R$'))
anos = int(input('Em quantos anos a dívida será negociada: '))

parcelas = vcasa / anos

#calculando 30% do salário

tsal = sal * 30 /100

if parcelas < tsal:
    print('{}, seu empréstimo foi aprovado! \nParcelas: {}X de R${} '.format('\033[35m', nome,'\033[m)', '\033[31m', anos, '\033[m', '\033[4;32m', parcelas, '\033[m'))
elif parcelas > tsal:
    print('Empréstimo negado! A cotação mensal excede os 30% do salário de {}'.format('\033[35m', nome, '\033[m'))
    print('Valor das parcelas: {}x de R${}'.format('\033[31m', anos, '\033[m', '\033[4;32m', parcelas, '\033[m'))
    print('30% do salário de R${}: R${}'.format('\033[36m', sal, '\033[m', '\033[31m', tsal))
print('Obrigado por utilizar nossos serviços! ')