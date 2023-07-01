import math
num = int(input('Informe um número: '))
raiz = math.sqrt(num)
print('A raiz quadrada de {} é igual a: {:.2f}'.format(num, raiz))
# math.ceil (Arredondar para cima)
print('A raiz quadrada de {} é igual a: {}'.format(num, math.ceil(raiz)))
# math.floor (Arredondar para baixo)
print('A raiz quadrada de {} é igual a: {}'.format(num, math.floor(raiz)))
