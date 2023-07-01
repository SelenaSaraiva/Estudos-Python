#Pedir uma entrada de valores x vezes e somá-los;

s = 0
for c in range(1,5): #vai de 1 a 4;
    n = int(input('Digite o {}° valor: '.format(c)))
    s = s + n #ou também s+=n
print('A soma de todos os valores informados é: {}'.format(s))