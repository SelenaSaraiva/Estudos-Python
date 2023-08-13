# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
# Faça também um programa que importe esse módulo e use algumas dessas funções.


# Def aumentar (10%); 
def aumentar (v, taxa): 
    reais = (v * taxa)/100 + v
    return reais


# Def diminuir (10%); 
def diminuir (v, taxa):
    reais = v - (v * taxa)/100 
    return reais


# Def dobro; 
def dobro (v): 
    reais = v * 2
    return reais


# Def metade; 
def metade (v): 
    reais = v / 2
    return reais

