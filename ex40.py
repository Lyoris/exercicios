n1 =float(input('Qual a primeira nota?'))
n2 =float(input('Qual é a primeira nota?'))
soma =(n1+n2)/2
if soma >= 5 and soma < 7:
    print('a média das notas são {}'.format(soma))
    print('RECUPERAÇÃO')
elif soma < 5:
    print('a média das notas são {}'.format(soma))
    print('REPROVADO')
elif soma > 7:
    print('a média das notas são {}'.format(soma))
    print('APROVADO')