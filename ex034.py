s =float(input('digite o salario atual: '))
ns =s + (s * 10)/100
ns15 =s +(s * 15)/100
if s >= 1250:
    print('o seu novo salário será de {:.2f}!'.format(ns))
else:
    print('o seu salário será de {:.2f}'.format(ns15))