"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""
variavel = 'ABC'

#Formatação simples; 
print(f'{variavel}')

#Preencher 10 espaços para a direita; 
print(f'{variavel: >10}')

#Preencher 10 espaços para a esquerda;
#OBS: o ponto serve para facilitar a visualização dos espaços; 
print(f'{variavel: <10}.')

#Centralizar, dentro de 10 espaços, a informação;
#OBS: Caso queira preencher com algo, basta colocar o símbolo depois dos :;  
print(f'{variavel: ^10}.')

print(f'{1000.4873648123746:0=+10,.1f}')

print(f'O hexadecimal de 1500 é {1500:08X}')

print(f'{variavel!r}')