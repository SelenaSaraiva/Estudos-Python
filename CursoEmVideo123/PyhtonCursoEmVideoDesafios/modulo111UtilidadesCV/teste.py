# ****Programa principal;****

# Biblioteca e importações; 
import moeda111
import dado112

# Entrada de valor pelo usuário; 
print('\033[36m=\033[m'*50)
valor = dado112.leiaDinheiro('Informe o valor a ser atualizado R$: ')
print('\033[36m=\033[m'*50)

moeda111.resumo(valor, 20, 12)
