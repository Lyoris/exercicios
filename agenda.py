from time import sleep
from colorama import Fore, Style,  init
init(autoreset=True)
agenda = {}
def adicionar_contato():
    while True:
        nome = input(Fore.LIGHTWHITE_EX+"Nome do contato (ou 'sair' para voltar ao menu): ").strip().title()
        if nome.lower() == "sair":
            break
        telefone = input(Fore.LIGHTWHITE_EX+"Telefone: ").strip()
        agenda[nome] = telefone
        print(Fore.LIGHTMAGENTA_EX+f"{nome} adicionado com sucesso!\n")
def buscar_contatos():
    nome =input(Fore.LIGHTWHITE_EX+'Digite o nome de busca: ').strip(). title()
    if nome in agenda:
        print(Fore.LIGHTMAGENTA_EX+f'{nome} - Telefone: {agenda[nome]}')
    else:
        print(Fore.LIGHTWHITE_EX+'O nome não está associado a lista de telefone! ')
def remover_contatos():
    nome = input(Fore.LIGHTWHITE_EX+'Digite um número para remover da agenda: ').strip(). title()
    if nome in agenda:
        del agenda[nome]
        print(Fore.LIGHTWHITE_EX+f'{nome} removido com sucesso!')
    else:
        print(Fore.LIGHTWHITE_EX+'Nome não encontrado!')
def listar_contatos():
    if agenda:
        print(Fore.LIGHTGREEN_EX+'======= Lista de contatos =======')
        for nome, telefone in agenda.items():
            print(Fore.LIGHTMAGENTA_EX+f'{nome}: {telefone}')
    if not agenda:
            print(Fore.LIGHTMAGENTA_EX+'Agenda vazia!!!')
def menu():
    while True:
        print(Fore.LIGHTWHITE_EX+'\n----- AGENDA DE CONTATOS -----')
        print(Fore.LIGHTWHITE_EX+'1. ADICIONAR CONTATOS')
        print(Fore.LIGHTWHITE_EX+'2. BUSCAR CONTATOS')
        print(Fore.LIGHTWHITE_EX+'3. REMOVER CONTATOS')
        print(Fore.LIGHTWHITE_EX+'4. LISTAR CONTATOS')
        print(Fore.LIGHTWHITE_EX+'5. SAIR')
        opcao =input(Fore.LIGHTMAGENTA_EX+"escolha uma opção: ")
        if opcao == '1':
            adicionar_contato()
        elif opcao == '2':
            buscar_contatos()
        elif opcao == '3':
            remover_contatos()
        elif opcao == '4':
            listar_contatos()
        elif opcao =='5':
            print(Fore.BLACK+'Saindo da agenda...')
            sleep(1)
            break
        else:
            print(Fore.BLACK+'opção inválida, tente novamente!')
menu()
