print('             Bem vindo(a) ao calculando rotas!              ')
print('-=-' * 20)

print('                 Informações de valores                   ')
print('Até 200km: R$0,50 POR QUILÔMETRO')
print('Acima de 200km: R$0,45 POR QUILÔMETRO')

print('-=-' * 20)
km = float(input('Informe a distância, em quilômetros(KM), da viagem? '))

if km <= 200:
    ate200 = km * 0.50
    print('Sua viagem ficará no valor de: R${} '.format(ate200))

else:
    cima200 = km * 0.45
    print('Sua viagem ficará no valor de: R${} '.format(cima200))

print('Obrigado! Dirija-se ao caixa. ')