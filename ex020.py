import random
name1 =str(input('digite primeiro nome'))
name2 =str(input('digite segundo nome'))
name3 =str(input('digite terceiro nome'))
name4 =str(input('digite quarto nome'))
nam =  [name1, name2, name3,name4]
random.shuffle(nam)
print('a ordem de apresentação será:')
for i, aluno in enumerate(nam, 1):
    print(f'{i}. {aluno}')
