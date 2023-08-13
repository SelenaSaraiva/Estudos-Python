# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('                   Analisando triâgulos!                          ')
print('-=-' * 20)

comp1 = float(input('Informe o primeiro comprimento: '))
comp2 = float(input('Informe o segundo comprimento: '))
comp3 = float(input('Informe o terceiro comprimento: '))

# analisando os comprimentos...

if comp1 < comp2 + comp3 and comp2 < comp1 + comp3 and comp3 < comp1 + comp2:
    print('As medidas informadas podem formar um triângulo!')

else:
    print('As medidas informadas não podem formar um triângulo!')