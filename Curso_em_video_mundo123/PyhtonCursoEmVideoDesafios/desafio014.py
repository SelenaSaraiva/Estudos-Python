# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit

c = float(input('Insira a temperatura em celsius:'))

f = c * 1.8 + 32

print('A temperatura de °{} graus celsiuis convertida em Fahrenheit é igual a: °{}'.format(c,f))