nome = str(input('Informe o nome do funcionário: '))
sal = float(input('Informe o salário do funcionário R$: '))

if sal > 1250:
    aumento = (sal * 10) / 100
    total = sal + aumento
    print("O seu salário sofreu um aumento de 10%. Você passará a receber: R${}".format(total))

if sal <= 1250:
    aumento = (sal * 15) / 100
    total = sal + aumento
    print('O seu salário sofreu um aumento de 15%. Você passrá a receber: R${}'.format(total))