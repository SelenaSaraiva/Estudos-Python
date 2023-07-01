print('\033[34m     Confederação Nacional de Natação (CNN)! \033[m        ')
print('\033[34m-=-\033[m'*20)

from datetime import date

print('Descubra sua categoria! Insira a baixo seu nome e seu ano de nascimento.')

nome = str(input('Nome completo: '))
nasc = int(input('Ano de nascimento: '))

print('\033[34m-=-\033[m'*20)

atual = date.today().year
categoria = atual - nasc

if categoria <= 9:
    print('O(A) atleta, {}, está na categoria \033[4;36mMIRIM!\033[m'.format(nome))
elif categoria == 10 or categoria <= 14:
    print('O(A) atleta, {}, está na categoria \033[4;35mINFANTIL!\033[m'.format(nome))
elif categoria == 15 or categoria <= 19:
    print('O(A) atleta, {}, está na categoria \033[4;33mJÚNIOR!\033[m'.format(nome))
elif categoria == 20 or categoria <= 25:
    print('O(A) atleta, {}, está na categoria \033[4;32mSÊNIOR!\033[m '.format(nome))
elif categoria > 25:
    print('O(A) atleta, {}, está na categoria \033[4;31mMASTER!\033[m'.format(nome))

print('\033[34m-=-\033[m'*20)



