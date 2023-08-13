print('               \033[33mCalculando descontos\033[m                ')
print('\033[33m-=-\033[m'*20)

preco = float(input('Insira o preço do produto: R$'))
print('\033[33m-=-\033[m'*20)

print('{1} Dinheiro/cheque \n{2} À vista no cartão \n{3} Até 2x no cartão \n{4} 3x ou mais ou cartão  ')
print('\033[33m-=-\033[m'*20)

opcao = int(input('Informe, entre as opções, a forma de pagamento: '))
print('\033[33m-=-\033[m'*20)

#escolhendo a opção 1
if opcao == 1:
    desconto = (preco * 10)/100
    total = preco - desconto
    print('Pagando em Dinheiro/cheque você possui 10% de desconto')
    print('Total: \033[4;34mR${:.2f}\033[m'.format(preco))
    print('Valor do desconto: \033[4;33mR$-{:.2f}\033[m'.format(desconto))
    print('Valor a ser pago: \033[4;32mR${:.2f}\033[m'.format(total))
#escolhendo a opção 2
elif opcao == 2:
    desconto = (preco * 5)/100
    total = preco - desconto
    print('Pagando à vista no cartão você possui 5% de desconto')
    print('Total: \033[4;34mR${:.2f}\033[m'.format(preco))
    print('Valor do desconto: \033[4;33m-R${:.2f}\033[m'.format(desconto))
    print('Valor a ser pago: \033[4;32mR${:.2f}\033[m'.format(total))
#escolhendo a opçao 3
elif opcao == 3:
    parcela = preco / 2
    print('Pagando em até 2x no cartão o valor não sofrerá alteração ')
    print('Total: \033[4;33mR${:.2f}\033[m'.format(preco))
    print('Valor a ser pago: \033[4;32m2x\033[m no valor de \033[4;32mR${:.2f}\033[m'.format(parcela))
#escolhendo a opçao 4
elif opcao == 4:
    prc = int(input('Informe a quantidade de parcelas: '))
    juros = (preco * 20)/100
    total = preco + juros
    parcela = total / prc
    print('Pagando em 3x ou mais no cartão, será cobrado 20% de juros ')
    print('Total: \033[4;34mR${:.2f}\033[m'.format(preco))
    print('Valor do juros: \033[4;33mR$+{:.2f}\033[m'.format(juros))
    print('Valor a ser pago: \033[4;32mR${:.2f}\033[m'.format(total))
    print('Ficará parcelado em \033[4;36m{}x\033[m de \033[4;36mR${:.2f}\033[m '.format(prc, parcela))
else:
    print('\033[31mOpção de pagamento inválida! Tente novamente.\033[m')
print('\033[33m-=-\033[m'*20)
print('Obrigado por utilizar nossos serviços!')