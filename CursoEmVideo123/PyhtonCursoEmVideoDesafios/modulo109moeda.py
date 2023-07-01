# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, 
# informando se o valor retornado por elas vai ser ou não formatado pela 
# função moeda(), desenvolvida no desafio 108.


# Def aumentar (10%); 
def aumentar (v = 0, taxa = 0, formate = False): 
    reais = (v * taxa)/100 + v
    return reais if not formate else moeda(reais) 


# Def diminuir (10%); 
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
