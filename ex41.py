from datetime import date
ano =int(input('ano de nascimento: '))
dat =date.today().year
res =dat - ano
if res < 9:
    print('--=--' * 20)
    print('O atleta tem {} anos.\n Classificação: MIRIM'.format(res))
    print('--=--' * 20)
elif res > 9 and res < 14:
    print('--=--' * 20)
    print('O atleta tem {} anos\n CLASSIFICAÇÃO: INFANTIL'.format(res))
    print('--=--' * 20)
elif res > 14 and res < 19:
    print('--=--' * 20)
    print('O  atleta tem {} anos\n CLASSIFICAÇÃO: JÚNIOR'.format(res))
    print('--=--' * 20)
elif res > 19 and res < 25:
    print('--=--' * 20)
    print('O  atleta tem {} anos\n CLASSIFICAÇÃO: SÊNIOR'.format(res))
    print('--=--' * 20)
else:
    print('--=--' * 20)
    print('O  atleta tem {} anos\n CLASSIFICAÇÃO: MASTER'.format(res))
    print('--=--' * 20)