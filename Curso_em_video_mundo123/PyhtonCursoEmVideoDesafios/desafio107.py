# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
# Faça também um programa que importe esse módulo e use algumas dessas funções.


# ****Programa principal;****

# Biblioteca e importações; 
import modulo107moeda

# Entrada de valor pelo usuário; 
print('\033[36m=\033[m'*50)
valor = int(input('Informe o valor a ser atualizado R$: '))
print('\033[36m=\033[m'*50)


print(f'\033[4;33mR${valor}\033[m com acréscimo de 10% é igual a: \033[4;33mR${modulo107moeda.aumentar(valor, 10)}\033[m') 
print(f'\033[4;33mR${valor}\033[m com um desconto de 10% é igual a: \033[4;33mR${modulo107moeda.diminuir(valor, 10)}\033[m') 
print(f'O dobro de \033[4;33mR${valor}\033[m é igual a: \033[mR${modulo107moeda.dobro(valor)}\033[m')
print(f'A metade de \033[4;33mR${valor}\033[m é igual a: \033[4;33mR${modulo107moeda.metade(valor)}\033[m')