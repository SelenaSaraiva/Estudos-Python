nome = input('Informe seu nome: ')
idade = int(input('Informe sua idade: '))

#Caso nome e idade com dados; 
if nome and idade:

    #Mostrar nome; 
    print(f'Seu nome é {nome}')

    #Inverter nome; 
    print(f'Seu nome invertido é: {nome[::-1]}')

    #Verificar a exitência de espaços; 
    if ' ' in nome: 
        print(f'O nome {nome} contém espaços!')
    else: 
        print(f'O nome {nome} não contém espaços!')

    #Quantidade de letras no nome; 
    print(f'Seu nome {nome} possui {len(nome)} letras!')

    #Primeira letra do nome; 
    print(f'A primeira letra do nome {nome} é {nome[0]}')

    print(f'A última letra do nome {nome} é {nome[-1]}')

#Caso nome e idade sem dados; 
else: 
    print('Desculpe, mas você deixou campos vazios!')


