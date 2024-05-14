# importando biblioteca OS para limpar tela; 
import os

# Lista para casdastro de restaurante; 
restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}] 

# Função com o nome do programa; 
def exibir_nome_do_programa(): 
      # Boas vindas ao usuário; 
      print('''\033[31m  
      █
      ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
      ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
      ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
      ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
      ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
      ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
            \033[m''')

# Função com as opções de escolha; 
def exibir_opcoes(): 
      # Exibir opções de escolha para o usuário; 
      print('''
1. CADASTRAR RESTAURANTE 
2. LISTAR RESTAURANTE 
3. ATIVAR RESTAURANTE 
4. SAIR \n''')

# Função para finalizar app (opção 4); 
def finalizar_app():
    # Limpando terminal e mostrando mensagem de subtítulo com função; 
    exibir_subtitulo('App finalizado')

# Função para voltar ao menu principal do programa; 
def voltar_ao_menu_principal(): 
      input('Digite \033[34mqualquer tecla\033[m para voltar ao \033[34mmenu principal:\033[m')
      main()

# Função para caso opção inválida do usuário; 
def opcao_invalida(): 
      print('Opção inválida!\n')
      voltar_ao_menu_principal()

# Função para limpar terminal e exibir mensagem de subtítulo; 
def exibir_subtitulo(texto): 
      os.system('cls')
      print(texto, '\n')

# Função para cadastrarmos um novo restaurante; 
def cadastrar_novo_restaurante():
      
      # Limpando terminal e mostrando mensagem de subtítulo com a função; 
      exibir_subtitulo('\033[36mCadastro de novos resturantes\033[m')

      # Entrando com o nome do resturante; 
      nome_do_restaurante = input('° Informe o nome do restaurante que deseja cadastrar: ')

      #Entrando com a categoria do restaurante; 
      categoria = input(f'Informe a categoria do restaurante {nome_do_restaurante}: ')

      # Criando dicionário de informações e adicionando na lista; 
      dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria':categoria, 'ativo':False}
      restaurantes.append(dados_do_restaurante)

      #mostrando mensagem de cadastro finalizado ao usuário; 
      print(f'\033[32mRestaurante {nome_do_restaurante} cadastrado com sucesso!\033[m')
      print('\n')

      # Voltando ao menu principal; 
      voltar_ao_menu_principal()

# Função para listarmos todos os nossos restaurantes existentes e cadastrados; 
def listar_restaurantes():

      #Limpando o terminal e mostrando mensagem de subtítulo com a função; 
      exibir_subtitulo('Restaurantes cadastrados')

      # Retornando os restaurantes, e sua informações, cadastrados na lista; 
      for restaurante in restaurantes: 
            nome_restaurante = restaurante['nome']
            categoria = restaurante['categoria']
            ativo = restaurante['ativo']
            print(f'- Restaurante: {nome_restaurante} | Categoria: {categoria} | Ativo: {ativo}') 
      
      print('\n')
      # Voltando ao menu principal; 
      voltar_ao_menu_principal()

# Função para alterar o estado "ativo(True)" ou "desativo(False) do restaurante" 
def alternar_estado_restaurante(): 
      exibir_subtitulo('Alterando estado do restaurante')
      nome_restaurante = input('Informe o nome do restaurante que deseja alternar o estado: ')
      restaurante_encontrado = False

      for restaurante in restaurantes: 
            if restaurante == restaurante['nome']:
                  restaurante_encontrado == True
                  restaurante['ativo'] = not restaurante['ativo']
                  mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso! ' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
                  print(mensagem)
      if not restaurante_encontrado: 
            print('Restaurante não encontrado!')

# Função para escolher e validar opção escolhida; 
def escolher_opcao(): 
      try: 
            # Entrada/escolha do usuário; 
            opcao_escolhida = int(input('Escolha uma opção: '))

            # Validando resposta de opções; 
            if (opcao_escolhida == 1): 
                  cadastrar_novo_restaurante() 

            elif (opcao_escolhida == 2): 
                  listar_restaurantes()

            elif (opcao_escolhida == 3): 
                  alternar_estado_restaurante()

            elif opcao_escolhida == 4: 
                  finalizar_app()
                  
            else: 
                  opcao_invalida() 
      except: 
            opcao_invalida()

# Função para mostragem das funções em ordem na tela; 
def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()   

if __name__ == '__main__': 
    main()