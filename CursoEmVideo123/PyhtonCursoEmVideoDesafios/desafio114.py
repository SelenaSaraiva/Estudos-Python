# Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

# Bibliotecas e importações; 
import urllib
import urllib.request

try: 
    site = urllib.request.urlopen('http://pudim.com.br')

except urllib.error.URLError:
    print('\033[4;31m O SITE NÃO ESTÁ ACESSÍVEL NO MOMENTO!\033[m')

else: 
    print('\033[4;32mSite visitado com sucesso!\033[m')
    print(site.read())

