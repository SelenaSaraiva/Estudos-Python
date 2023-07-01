#AULA 14
#EXE 03;
#Enquanto a resposta for sim(s) peça um valor;

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Deseja continuar? [S/N]')).upper()
print('Fim')