# Crie um programa onde o usuário digite uma expressão qualquer
# que use parênteses. Seu aplicativo deverá analisar se a expressão
# passada está com os parênteses abertos e fechados na ordem correta.

# Definindo listas;
algebra = []

# Declarações e variáveis;
abertoP = 0
fechadoP = 0

# Entrada da expressão pelo usuário;
expressao = str(input('Digite sua expressão com parenteses: '))

for simb in expressao:

    # Contando parenteses abertos;
    if simb == '(':
        abertoP += 1

    # Contando parenteses fechados;
    elif simb == ')':
        fechadoP += 1

algebra.append(expressao)

if abertoP == fechadoP:
    print(f'\033[4;32mEXPRESSÃO VÁLIDA!\n\033[33m{algebra}\033[m\033[m')

else:
    print(f'\033[4;31mEXPRESSÃO INVÁLIDA!\033[m\n Verificar parenteses \033[33m{algebra}\033[m\033[m')