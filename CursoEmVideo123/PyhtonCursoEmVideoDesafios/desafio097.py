# Faça um programa que tenha uma função chamada escreva(), que receba 
# um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. 
# Ex: escreva(‘Olá, Mundo!’) 
# Saída:  ~~~~~~~~~  
#        Olá, Mundo! 
#        ~~~~~~~~~   



# Entrada de informação pelo usuário; 
info = str(input('Digite algo: '))

# Obtendo o tamanho do texto; 
tamanho = len(info)

# Def; 
def escreva(txt):
    print('='*tamanho)
    print(f'  {txt}')
    print('='*tamanho)

# Programa principal; 
escreva(info)

