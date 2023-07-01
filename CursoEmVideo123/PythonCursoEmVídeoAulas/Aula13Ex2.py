#contagem contralada pelo usuário. Início, fim e passos;

i = int(input('Digite o início da contagem: '))
f = int(input('Digite o fim da contagem: '))
p = int(input('Digite o passo da contagem: '))
print('\033[36m-=-\033[m'*20)

for c in range (i, f+1, p):
    print(c)
print('\033[36m-=-\033[m'*20)
print('\033[36mFim da contagem!\033[m')
