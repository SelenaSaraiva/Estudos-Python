# Adapte o código do desafio #107, criando uma função adicional chamada moeda() 
# que consiga mostrar os números como um valor monetário formatado.


# Def aumentar (10%); 
def aumentar (v = 0, taxa = 0): 
    reais = (v * taxa)/100 + v
    return reais


# Def diminuir (10%); 
def diminuir (v = 0, taxa = 0):
    reais = v - (v * taxa)/100 
    return reais


# Def dobro; 
def dobro (v = 0): 
    reais = v * 2
    return reais


# Def metade; 
def metade (v = 0): 
    reais = v / 2
    return reais

# Def moeda;
def moeda(v = 0, moeda = 'R$'):
    return f'{moeda}{v:.2f}'.replace('.', ',')

