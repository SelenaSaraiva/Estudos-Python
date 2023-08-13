# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite o seu nome completo: ')).strip()
div = nome.split()

print("O seu primeiro nome é: {} ".format(div[0]))
print('O seu último nome é: {} '.format(div[len(div)-1]))



