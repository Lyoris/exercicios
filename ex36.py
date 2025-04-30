print('-=-'*20)
casa =float(input('digite o valor da casa: '))
print('-=-'*20)
salario =float(input('digite o seu salário:'))
print('-=-'*20)
anos =int(input('em quantos anos deseja pagar?'))
print('-=-'*20)
parcela =casa /(anos * 12)
minimo = salario * 30 / 100
print('para pagar uma casa de {:.2f} em {} anos'.format(casa, anos), end='')
print(' a prestação será de R${:.2f}'.format(parcela))
if parcela <= minimo:
    print('você pode financiar a casa!')
else:
    print('seu salario é incompativel com a prestação!')