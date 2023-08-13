# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, 
# informando se o valor retornado por elas vai ser ou não formatado pela 
# função moeda(), desenvolvida no desafio 108.




# ****Programa principal;****

# Biblioteca e importações; 
import modulo109moeda

# Entrada de valor pelo usuário; 
print('\033[36m=\033[m'*50)
valor = int(input('Informe o valor a ser atualizado R$: '))
print('\033[36m=\033[m'*50)


# Visualização do usuário; 
print(f'\033[4;33m{modulo109moeda.moeda(valor)}\033[m com acréscimo de 10% é igual a: \033[4;33m{modulo109moeda.aumentar(valor, 10, True)}\033[m') 
print(f'\033[4;33m{modulo109moeda.moeda(valor)}\033[m com um desconto de 10% é igual a: \033[4;33m{modulo109moeda.diminuir(valor, 10, True)}\033[m') 
print(f'O dobro de \033[4;33m{modulo109moeda.moeda(valor)}\033[m é igual a: \033[m{modulo109moeda.dobro(valor, True)}\033[m')
print(f'A metade de \033[4;33m{modulo109moeda.moeda(valor)}\033[m é igual a: \033[4;33m{modulo109moeda.metade(valor, True)}\033[m')