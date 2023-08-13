teste = []
teste.append('SELENA')
teste.append(20)

galera = []
galera.append(teste[:])
teste[0] = 'Geaz'
teste[1] = 23
galera.append(teste[:])

print(galera)
