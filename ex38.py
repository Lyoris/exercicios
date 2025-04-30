p1 =float(input('PRIMEIRO NÚMERO: '))
p2 =float(input('SEGUNDO NUMERO'))
if p1 > p2:
    print(f'O maior número é {p1}')
elif p2 > p1:
    print(f'O maior numero é {p2}')
elif p1 == p2 or p2 == p1:
    print('Ambos são iguais')