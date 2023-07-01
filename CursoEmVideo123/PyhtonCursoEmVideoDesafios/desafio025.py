nome = str(input('Informe o seu nome completo: ')).strip()

print('O nome, {}, possui o sobrenome SILVA!? {}'.format(nome, nome.find('Silva')))

# Segunda forma de execução

nome = str(input('Informe o seu nome completo: ')).strip()

print('O nome, {}, possui o sobrenome SILVA!? {}'.format(nome, 'SILVA' in nome.upper()))