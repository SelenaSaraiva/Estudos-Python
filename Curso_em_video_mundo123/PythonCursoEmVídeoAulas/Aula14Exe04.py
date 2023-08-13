#AULA 14
#EXE 04;
#Enquanto n for diferente de 0 veja, se não for 0, se o
#número digitados é par ou impar;

n = 1
par = impar = 0

while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par = par + 1 #par += 1
        else:
            impar = impar + 1 #impar += 1
print('Você digitou {} números PARES e {} números ímpares'.format(par, impar))