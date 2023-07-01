# Adicione o módulo moeda.py criado nos desafios anteriores, uma função 
# chamada resumo(), que mostre na tela algumas informações geradas pelas 
# funções que já temos no módulo criado até aqui.


# Def aumentar; 
def aumentar (v = 0, taxa = 0, formate = False): 
    reais = (v * taxa)/100 + v
    return reais if not formate else moeda(reais) 


# Def diminuir; 
def diminuir (v = 0, taxa = 0, formate = False):
    reais = v - (v * taxa)/100 
    return reais if not formate else moeda(reais)


# Def dobro; 
def dobro (v = 0, formate = False): 
    reais = v * 2
    return reais if not formate else moeda(reais)

# Def metade; 
def metade (v = 0, formate = False): 
    reais = v / 2
    return reais if not formate else moeda(reais)

# Def moeda;
def moeda(v = 0, moeda = 'R$'):
    return f'{moeda}{v:.2f}'.replace('.', ',')

# Def resumo; 
def resumo(v = 0, taxaA = 10, taxaD = 5):
    print('-'*40)
    print('RESUMO DO VALOR'.center(40)) 
    print('-'*40)
    print(f'VALOR ANALISADO: \t{moeda(v)}')
    print(f'DOBRO DO VALOR: \t{dobro(v, True)}')
    print(f'METADE DO VALOR: \t{metade(v, True)}')
    print(f'{taxaA}% DE AUMENTO: \t{aumentar(v, taxaA, True)}')
    print(f'{taxaD}% DE REDUÇÃO: \t{diminuir(v, taxaD, True)}')
    print('-'*40)
              