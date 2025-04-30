grupo = []
while True:
    pessoas = []
    pes =input('Digite o nome do aluno: ')
    nome =float(input('Digite a nota do aluno: '))
    nomes =float(input('Digite a nota do aluno: '))
    nomess =float(input('Digite a nota do aluno: '))
    media = (nome + nomes + nomess) / 3
    grupo.append([pes, [nome, nomes, nomess], media])
    exit =input('Deseja continuar? [S/N]').upper(). upper()

    if exit == 'N':
        break
print('-='*15)
print(f'{'No.':<4}{'NOME':<10}{"MÉDIA":>8}')
print('-'*30)
for i, p in enumerate(grupo, start=0):
    print(f'{i:<4}{p[0]:<10}{media:>8.1f} ')
while True:
    print('-'*35)
    opc =int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opc == 999:
        break
    if opc <= len(grupo) - 1:
        print(f' Notas de {grupo[opc][0]} são {grupo[opc][1]}')
print('<<<<< VOLTE SEMPRE >>>>>')