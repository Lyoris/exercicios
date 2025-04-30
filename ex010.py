r =float(input('Quanto dinheiro você tem na carteira? R$'))
c = r/5.887
ce = r/6.45
print('com R${:.2f} você pode comprar US${:.2f}\ncom R${:.2f} você pode comprar €{:.2f}'.format(r, c, r, ce))