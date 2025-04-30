P =float(input('qual o preço do produto?'))
Po =float(input('qual a porcentagem de desconto?'))
D = P * (Po/100)
PD = P - D
print('O produto que custava R${}, na promoção com desconto de {}% vai custar R${:.2f}.'.format(P,Po, PD))