print("Digite seu nome: ")
nome = input()
print("Digite o seu sobrenome: ")
sobrenome = input()
print("Entre com suas quatro notas: ")
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
nota4 = float(input())
media = (nota1+nota2+nota3+nota4)/4
if media >=7:
    print("Olá, " + nome + sobrenome + "!" + " Sua média final é: " + str(media) + "." + "Parabéns, você foi aprovado(a)!")
else:
    print("Que pena, " + nome + sobrenome + "!" + " Sua média final é: " + str(media) + "." + " Você está reprovado(a)!") 
    
