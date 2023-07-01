# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

# Valor da diária: 60R$
# Valor por Km percorridos: 0,15R$

print('                                                         Bem vindo(a) a locadora de automóveis!                                                               ')
print('-----------------------------------------------------------------------------------------------------------------------------------------------')

nome = input('Informe o nome do automóvel: ')

marca = input('Informe a marca do automóvel: ')

placa = input('Informe a placa do automóvel: ')

km = float(input('Informe a quantidade de Km (quilômetros) percorridos: km'))

dias = int(input('Informe por quantos dias o carro foi alugado: '))

vd = dias * 60
vkmp = km * 0.15
total = vd + vkmp

print('-----------------------------------------------------------------------------------------------------------------------------------------------')
print(' Carro: {} \n Marca: {} \n Placa: {}\n Pagará {:.2f}R$ pela diária e {:.2f}R$ pelos quilômetros percorridos.\n Total: {:.2f}R$'.format(nome, marca, placa, vd, vkmp, total))
