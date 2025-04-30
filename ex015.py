# diaria de 100$ e taxa a cada 1km de 0,03$
d =int(input('Quantos dias alugados?'))
km =float(input('quantos KM rodados?'))

t = (d * 100) + (0.03 * km)
print('-'*32)
print('O total a pagar é de R${:.2f}'.format(t))
print('-'*32)