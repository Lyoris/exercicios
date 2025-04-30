num = list()
par =list()
impar = list()
while True:
    num.append(int(input('digite um numero ')))
    resp =str(input('quer continuar?[S/N]'))
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print('-='*30)
print(f'a lista completa é {num}')
print(f'a lista de par é {par}')
print(f'a lista de impares é {impar}')
print('-='*30)