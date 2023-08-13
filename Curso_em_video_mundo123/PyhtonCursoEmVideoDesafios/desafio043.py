print('                 \033[1;36mIMC\033[m                    ')
print('\033[36m-=-\033[m'*15)

nome = str(input('Informe o seu nome: '))

print('\033[36m-=-\033[m'*15)

print('Certo, {}. Para começarmos a calcular seu IMC, nos informe suas medidas'.format(nome))

print('\033[36m-=-\033[m'*15)

peso = float(input('Peso (kg): '))
altura = float(input('Altura (M): '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('{}, você se encontra \033[4;33mABAIXO DO PESO!\033[m Procure ajuda de um profissional.'.format(nome))
elif imc >= 18.5 and imc < 25: # 18.5 <= imc < 25 - outra forma
    print('{}, você se encontra no seu \033[4;32mPESO IDEAL!\033[m'.format(nome))
elif imc >= 25 and imc <= 30: # 25 >= imc <= 30 - outra forma
    print('{}, você se encontra em \033[4;93mSOBREPESO!\033[m Procure ajuda de um profissional. '.format(nome))
elif imc >= 30 and imc <= 40: # 30 >= imc <= 40 - outra forma
    print('{}, você se encontra em estado de \033[4;91mOBESIDADE!\033[m Procure ajuda de um profissional.'.format(nome))
elif imc > 40:
    print('{}, você se encontra em \033[4;31mOBESIDADE MÓRBIDA!\033[m Procure urgente ajuda de um profissional.\033[m'.format(nome))

print('Seu IMC: {:.1f} '.format(imc))
print('\033[36m-=-\033[m'*15)
print('\033[4mObrigado por utilizar nossos serviços!\033[m')