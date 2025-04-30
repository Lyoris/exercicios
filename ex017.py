import math
cato =float(input('digite o cateto oposto'))
cata =float(input('digite o cateto adjacente'))
hipo = math.sqrt(cato**2 + cata**2)
print('a hipotenusa é {:.2f}'.format(hipo))
