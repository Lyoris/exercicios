from datetime import date
atual =date.today().year
ano =int(input('Ano de nascimento: '))
idade =atual - ano
print('Quem nasceu em {} tem {} ano(s) em {}'.format(ano, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!!!')
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado a {} anos!!!'.format(saldo))
elif idade < 18:
    saldo = idade - 18
    print('Você ainda tem {} anos até o alistamento'.format(saldo))