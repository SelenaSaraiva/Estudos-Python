# Adapte o código do desafio #107, criando uma função adicional chamada moeda() 
# que consiga mostrar os números como um valor monetário formatado.


# ****Programa principal;****

# Biblioteca e importações; 
import modulo108moeda

# Entrada de valor pelo usuário; 
print('\033[36m=\033[m'*50)
valor = int(input('Informe o valor a ser atualizado R$: '))
print('\033[36m=\033[m'*50)


# Visualização do usuário; 
print(f'\033[4;33m{modulo108moeda.moeda(valor)}\033[m com acréscimo de 10% é igual a: \033[4;33m{modulo108moeda.moeda(modulo108moeda.aumentar(valor, 10))}\033[m') 
print(f'\033[4;33m{modulo108moeda.moeda(valor)}\033[m com um desconto de 10% é igual a: \033[4;33m{modulo108moeda.moeda(modulo108moeda.diminuir(valor, 10))}\033[m') 
print(f'O dobro de \033[4;33m{modulo108moeda.moeda(valor)}\033[m é igual a: \033[m{modulo108moeda.moeda(modulo108moeda.dobro(valor))}\033[m')
print(f'A metade de \033[4;33m{modulo108moeda.moeda(valor)}\033[m é igual a: \033[4;33m{modulo108moeda.moeda(modulo108moeda.metade(valor))}\033[m')