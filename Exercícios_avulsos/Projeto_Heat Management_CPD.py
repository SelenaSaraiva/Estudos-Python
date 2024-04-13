print("Bem vindo(a) ao projeto Heat Management! Vamos começar a verificação da temperatura ideal do seu Data_Center.")
print("Digite a temperatura atual do seu CPD:")
ti = float(input())
if ti <= 18:
    print("Excelente! A temperatura do seu CPD está dentro da faixa operacional indicada para uso.")
elif ti <= 27:
     print("Excelente! A temperatura do seu CPD está dentro da faixa operacional indicada para uso.")
else:
    print("Atenção! O calor excessivo pode queimar equipamentos ou provocar o autodesligamento da máquina. Recomendamos manter a temperatura entre 18°C a 27°C! ")         
