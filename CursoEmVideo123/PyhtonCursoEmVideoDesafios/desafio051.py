#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#No final, mostre os 10 primeiros termos dessa progressão.

print('            PROGRESSÃO ARITMÉTICA              ')
print('\033[91m-=-\033[m'*20)

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

#descobrindo os 10 primeiros termos;
decimo = primeiro + (10 - 1) * razao

for c in range(primeiro, decimo, razao):
    print('\033[91m{}\033[m'.format(c), end='-> ')
print('Fim')