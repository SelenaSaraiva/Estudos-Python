from datetime import date

atual = date.today().year
nasc = int(input('Informe seu ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))

if idade == 18:
    print('Você precisa se alistar imediatamente!')
elif idade < 18:
    cal = 18 - idade
    print('Ainda faltam {} anos para o seu alistamento.'.format(cal))
    ano = atual + cal
    print('O seu alistamento será em {}'.format(ano))
elif idade > 18:
    cal = idade - 18
    print('Seu alistamento deveria ter ocorrido há {} anos'.format(cal))
    ano = atual - cal
    print('O seu alistamento foi em {} '.format(ano))