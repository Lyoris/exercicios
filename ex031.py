d =float(input('digite a distancia da viagem em Quilometros:'))
p =0.50 * d
pe =0.45 * d
if d <= 200:
    print(f'o valor da viagem será de {p}, tenha uma boa noite!')
else:
    print(f'o valor da viagem será de {pe}, tenha uma boa noite!')
