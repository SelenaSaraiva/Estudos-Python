# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

print('                Analisando triângulos              ')
print('\033[33m-=-\033[m' * 20)

comp1 = float(input('Informe o primeiro comprimento: '))
comp2 = float(input('Informe o segundo comprimento: '))
comp3 = float(input('Informe o terceiro comprimento: '))

print('\033[33m-=-\033[m' * 20)

# Analisando os comprimentos

if comp1 < comp2 + comp3 and comp2 < comp1 + comp3 and comp3 < comp1 + comp2:
    print('As medidas informadas podem formar um triângulo!')

    # descobrindo o tipo de triângulo
    if comp1 == comp2 == comp3:  # novo jeito de realizar análise
        print('Tipo do triângulo: \033[4;33mEQUILÁTERO!\033[m')
    elif comp1 != comp2 != comp3 != comp1:  # novo jeito de realizar análise
        print('Tipo do triângulo: \033[4;34mESCALENO!\033[m')
    else:
        print('Tipo do triângulo: \033[4;36mISÓSCELES!\033[m')
else:
    print('Os comprimentos informados não podem formar um triângulo!')