from colorama import Fore, Style
import time
import sys
usuarios = {}


def escrever(texto, delay=0.05):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def cadastrar_usuario():
    print(Fore.CYAN + "\n=== CADASTRO DE NOVO USUÁRIO ===" + Style.RESET_ALL)

    while True:
        usuario = input("Digite um nome de usuário: ").strip()
        if usuario in usuarios:
            print(Fore.RED + "Esse nome já está em uso. Tente outro." + Style.RESET_ALL)
        elif usuario == "":
            print(Fore.RED + "O nome de usuário não pode ser vazio." + Style.RESET_ALL)
        else:
            break

    while True:
        senha = input("Digite uma senha: ")
        confirmar = input("Confirme a senha: ")
        if senha != confirmar:
            print(Fore.RED + "As senhas não coincidem. Tente novamente." + Style.RESET_ALL)
        elif len(senha) < 4:
            print(Fore.RED + "A senha deve ter pelo menos 4 caracteres." + Style.RESET_ALL)
        else:
            break

    usuarios[usuario] = {"senha":senha}

    print(Fore.GREEN + f"Usuário '{usuario}' cadastrado com sucesso!\n" + Style.RESET_ALL)

def menu():
    while True:
        print(Fore.YELLOW + '=' * 35 + Style.RESET_ALL)
        print(Fore.LIGHTWHITE_EX + '         SISTEMA DE LOGIN'.upper() + Style.RESET_ALL)
        print(Fore.YELLOW + '=' * 35 + Style.RESET_ALL)
        print(Fore.LIGHTWHITE_EX + '[1] CADASTRAR NOVO USUÁRIO' + Style.RESET_ALL)
        print(Fore.LIGHTWHITE_EX + '[2] LOGIN' + Style.RESET_ALL)
        print(Fore.LIGHTWHITE_EX + '[3] SAIR' + Style.RESET_ALL)
        resp = input(Fore.LIGHTMAGENTA_EX + 'Digite sua escolha: ' + Style.RESET_ALL).strip()

        if not resp.isdigit() or int(resp) not in (1, 2, 3):
            print(Fore.RED + 'Opção inválida, tente novamente.\n' + Style.RESET_ALL)
            continue

        resp = int(resp)

        if resp == 1:
            cadastrar_usuario()
        if resp == 2:
            login()
        if resp == 3:
            saida()
def login():

        while True:
            print('=' * 20)
            print('LOGIN')
            print('=' * 20)
            log =input(Fore.LIGHTWHITE_EX + 'digite o nome de usuário: ' .strip() + Style.RESET_ALL)
            sen = input(Fore.LIGHTWHITE_EX + 'digite a senha: '.strip() + Style.RESET_ALL )
            if log in usuarios and usuarios[log]["senha"] == sen:
                escrever(Fore.LIGHTGREEN_EX + f'acesso autorizado com sucesso! Bem-vindo {log}\n')
            else:
                escrever(Fore.RED + 'Login ou senha inválidos.\n')
            time.sleep(1)
            break
            print(Fore.LIGHTGREEN_EX + f"Usuário '{log}' logado com sucesso!\n" + Style.RESET_ALL)
def saida():
    print(Fore.LIGHTMAGENTA_EX, end="")
    escrever( 'obrigado por participar do nosso serviço, volte sempre!', delay=0.03)
    escrever('PROCESSANDO SAÍDA.....', delay=0.03)
    print(Style.RESET_ALL)
    exit()


# Executa o menu
menu()