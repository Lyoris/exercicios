import random
name =str(input('digite o primeiro nome:'))
name2 =str(input('digite outro nome:'))
name3 =str(input('digite outro nome'))
name4 =str(input('digite outro nome:'))
nomes = name, name2, name3, name4
aleatorio = random.choices(nomes)
print('O aluno sorteado para apagar o quadro foi o {}!'.format(aleatorio))
