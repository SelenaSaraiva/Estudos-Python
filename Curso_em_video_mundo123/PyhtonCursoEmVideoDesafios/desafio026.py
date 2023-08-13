frase = str(input('Digite uma frase: ')).upper().strip()

print('Dentro da frase informada, a letra A está presente {} vezes. '.format(frase.count('A')))
print('--------------------------------------------------------------------')

print('A primeira letra A que aparece na frase, encontra-se na posição: {}'.format(frase.find('A')+1))
print('--------------------------------------------------------------------')

print('A última letra A presente na frase, encontra-se na posição: {}'.format(frase.rfind('A')+1))