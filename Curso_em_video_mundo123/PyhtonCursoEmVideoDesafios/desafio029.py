print('             Bem vindo(a) ao radar eletrônico!          ')
print('----------------------------------------------------------------------------')
print('A velocidade permitida é 80km/h. Se caso esse limite for excedido, será cobrado R$7,00 por quilômetro ultrapassado.')
print('Todos os valores retornados serão baseados nos valores acima e quilometragem informada.')
print('----------------------------------------------------------------------------')

print('Informações do veículo a ser analisado')
placa = str(input('Informe a placa do veículo: '))
km = float(input('Informe a velocidade do veículo:KM/H '))
print('----------------------------------------------------------------------------')

if km > 80:
    kmult = km - 80
    multa = kmult * 7
    print('Limite de velociade excedido! O veículo informado ultrapassou {} Km/h.'.format(kmult))
    print('Placa do automóvel: {}'.format(placa.upper()))
    print('Valor da multa: R${}'.format(multa))

else:
    print('O veículo informado está dentro do limite de velocidade permitida!')