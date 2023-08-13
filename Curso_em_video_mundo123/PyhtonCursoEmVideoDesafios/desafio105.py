# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações:
# Quantidade de notas; A maior nota; A menor nota; A média da turma; A situação (opcional)

# Apresentações; 
print('\033[34m==============================\033[m')
print('\033[34m          BOLETIM\033[m')
print('\033[34m==============================\033[m')


# Definindo dicinário; 
boletim = {}

# Def; 
def notas(*dic, sit=False): 
    '''Função para análise de notas e situação de uma turma
    :para dic: recebe uma ou mais notas
    :para sit: valor de uso opcional. Responsável por mostrar a situação da turma
    :para boletim: dicionário onde as informações estão armazenadas '''

    # descobrindo a média da turma; 
    c = 0
    for v in dic:
        c += v 
    
    media = c / 4

    # Estrutarando dicionário;
    boletim['Total de notas: '] = len(dic)
    boletim['Maior nota'] = max(dic)
    boletim['Menor nota'] = min(dic)
    boletim['Média da turma'] = media

    # Estruturando situação da turma(opcional); 
    if sit:

        if media <= 5: 
            boletim['Situação: '] = 'RUIM'
        
        elif media <= 7: 
            boletim['Situação:'] = 'BOM'
        
        elif media > 7: 
            boletim['Situação:'] = 'MUITO BOM'
     


# Programa principal; 
notas(10.0, 9.0, 8.0, 3.0, sit=True)
print(boletim)


