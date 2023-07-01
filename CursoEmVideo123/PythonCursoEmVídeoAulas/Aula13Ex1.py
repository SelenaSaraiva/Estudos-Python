#contando de 0 até o número inserido pelo usuário;

n = int(input('Digite o número final da contagem: '))
print('\033[36m-=-\033[m'*20)

for c in range (0, n + 1):
    print(c)
print('\033[36m-=-\033[m'*20)
print('\033[36mFim da contagem!\033[m')