print('  \033[33m                  *Serviço militar*                      ')
print('\033[33m-=-' * 20, '\033[m')

idade = int(input('Informe sua idade: '))

# Calculando tempo restante para se alistar(dois calculos para não dar resultados negativos no maior)

if idade <= 18:
    anos = 18 - idade
elif idade > 18:
    anos2 = idade - 18

#Condições de alistamento conforme idade;

if idade <= 16:
    print('Você ainda não tem idade para se alistar. \nAlistamento previsto para: {} {}'.format(anos, 'anos'))
elif idade == 17:
    print('Alistamento próximo. Você deverá se alistar no ano do seu aniversário de 18 anos.')
elif idade == 18:
    print('Atenção! Hora de se alistar. Compareça ao quartel mais próximo e apresente-se o mais breve possível!')
elif idade > 18:
    print('Alistamento em atraso! Você deveria ter se alistado há {} {}. '.format(anos2, 'anos'))


