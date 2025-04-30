alunos = []
valor = list()
while True:
        nome=input('Digite o nome do aluno')
        nota1=float(input('Digite a nota do aluno: '))
        nota2=float(input('digite a segunda nota: '))
        media =(nota1+nota2)/2
        aluno ={
            'nome':nome,
            "notas":[nota1, nota2],
            "media": media,
            "status":"aprovado" if media >= 7  else "reprovado"
        }
        alunos.append(aluno)
        cont = input('Deseja continuar? [S/N]').strip() .upper()
        if cont != 'S':
            break
for aluno in alunos:
    print(f'o aluno {aluno["nome"]} teve suas notas {aluno["notas"]} e está {aluno["status"]}.')
    print('encerrando o programa...')


