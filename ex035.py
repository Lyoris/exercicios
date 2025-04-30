a =float(input('digite a primeira reta'))
b =float(input('digite a segunda reta'))
c =float(input('digite a ultima reta'))
if a  + b > c and a + c > b and b + c > a:
    print('as retas PODEM formar um  triangulo')
else:
    print('as retas não podem formar um triangulo')
