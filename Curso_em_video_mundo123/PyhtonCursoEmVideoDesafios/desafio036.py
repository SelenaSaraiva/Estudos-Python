print('                    Empréstimo bancário!                    ')
print('-=-'*20)
print('Olá! Seja bem vindo(a)! Para começarmos a calcular seu empréstimo, precisaremos \nde algumas informações. Vamos lá?')
print('-=-'*20)

nome = str(input('Digite o seu nome: '))
vcasa = float(input('Informe o valor do imóvel: R$'))
sal = float(input('Informe o seu salário: R$'))
anos = int(input('Em quantos anos a dívida será negociada: '))
print('-=-'*20)

parcelas = vcasa / (anos * 12)

#calculando 30% do salário

tsal = sal * 30 /100

if parcelas < tsal:
    print('{}, seu empréstimo foi aprovado! \nParcelas: {}X de R${:.2f} '.format(nome, anos, parcelas))
elif parcelas > tsal:
    print('Empréstimo negado! A cotação mensal excede os 30% do salário de {}'.format(nome))
    print('Valor das parcelas: {}x de R${:.2f}'.format(anos, parcelas))
    print('30% do salário de R${}: R${:.2f}'.format(sal, tsal))
print('Obrigado por utilizar nossos serviços! ')