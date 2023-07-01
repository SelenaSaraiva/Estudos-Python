#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

produto = float(input('Informe o valor do produto: R$'))
desc = float(input('Informe a % do desconto: %'))

conta = (produto * desc)/100
precoAtuali = produto - conta

print('O produto no valor de R${:.2f} recebeu um desconto de {}% e passou a custar: {:.2f}'.format(produto, desc, precoAtuali))
