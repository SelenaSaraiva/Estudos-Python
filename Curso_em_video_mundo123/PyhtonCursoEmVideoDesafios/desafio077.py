# Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

# Tupla com palavras;
palavras = ('Computador', 'Whey', 'Fisica', 'Alien', 'Gamer', 'Livro',
            'Tatuagem', 'Jogo', 'Nave', 'Viajem', 'Estrada', 'Programar')

# Identificando e mostrando vogais;
for pala in palavras:
    print(f'Palavra \033[4;33m{pala}\033[m \nSua(s) vogais: ', end= '')
    for letra in pala:
        if letra.lower() in 'aeiou':
            print(f'\033[4;33m{letra}\033[m', end=' ')
    print('\n ')