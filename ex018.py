import math
angulo =float(input('digite um angulo para saber sobre seu seno e coseno'))
angulos = math.radians(angulo)
seno = math.sin(angulos)
coseno = math.cos(angulos)
tang = math.tan(angulos)
print('O seno do angulo {} é {}\n o coseno é {}\n a tangente é {}'.format(angulo, seno, coseno, tang))