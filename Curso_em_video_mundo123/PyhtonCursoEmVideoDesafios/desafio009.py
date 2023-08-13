# Tabuada de um número qualquer

tab = int(input('Informe o número da tabuada desejada: '))
cont = 0

print('Tabuada do número {}'.format(tab))

while cont <= 10:
    print('{} x {} =  {}'.format(tab, cont, (tab * cont)))
    cont = cont + 1


