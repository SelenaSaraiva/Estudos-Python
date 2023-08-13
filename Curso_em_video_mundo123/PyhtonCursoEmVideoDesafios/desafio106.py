# Def ajuda; 
def ajuda (coman): 
    help(coman)

# Def titulo; 
def titulo (msg, cor=0): 
    tam = len(msg) + 4
    print('=' * tam)
    print(f' {msg}')
    print('=' * tam)


# Programa principal; 
comando = ''
while True:
    titulo ('\033[31mSISTEMA DE AJUDA PYHELP\033[m')
    comando = str(input('Informe função ou biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else: 
        ajuda(comando)


# Um help em cores; 