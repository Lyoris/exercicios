import os

alunos = []

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def cadastrar_aluno():
    limpar_tela()
    print("=== CADASTRO DE ALUNO ===")
    nome = input("Nome do aluno: ").strip()
    idade = int(input("Idade: "))
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    media = (nota1 + nota2) / 2
    aluno = {
        'nome': nome,
        'idade': idade,
        'notas': [nota1, nota2],
        'media': media
    }
    alunos.append(aluno)
    print(f"\nAluno {nome} cadastrado com sucesso!")
    input("\nPressione ENTER para voltar ao menu...")

def listar_alunos():
    limpar_tela()
    print("=== LISTA DE ALUNOS ===")
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for i, aluno in enumerate(alunos):
            print(f"{i+1}. {aluno['nome']} - {aluno['idade']} anos - Média: {aluno['media']:.2f}")
    input("\nPressione ENTER para voltar ao menu...")

def mostrar_menu():
    while True:
        limpar_tela()
        print("=== SISTEMA DE CADASTRO DE ALUNOS ===")
        print("1. Cadastrar aluno")
        print("2. Listar alunos")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_aluno()
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida!")
            input("Pressione ENTER para tentar novamente...")

# Inicia o programa
mostrar_menu()