# Adicione o módulo moeda.py criado nos desafios anteriores, uma função 
# chamada resumo(), que mostre na tela algumas informações geradas pelas 
# funções que já temos no módulo criado até aqui.


# ****Programa principal;****

# Biblioteca e importações; 
import modulo110moeda 

# Entrada de valor pelo usuário; 
print('\033[36m=\033[m'*50)
valor = int(input('Informe o valor a ser atualizado R$: '))
print('\033[36m=\033[m'*50)

modulo110moeda.resumo(valor, 20, 12)



