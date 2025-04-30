import random
from time import sleep

# Função para exibir o menu
def mostrar_menu():
    print('\nEscolha uma opção:')
    print('[1] Somar')
    print('[2] Multiplicar')
    print('[3] Maior')
    print('[4] Gerar novos números aleatórios')
    print('[5] Sair do programa')
    print('[6] Trocar números manualmente')

# Entrada inicial de números
n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))

# Loop principal do programa
while True:
    mostrar_menu()
    per = int(input('Digite sua opção: '))

    if per == 1:
        soma = n1 + n2
        print(f'A soma dos valores é {soma}.')
    elif per == 2:
        multiplicacao = n1 * n2
        print(f'A multiplicação dos valores é {multiplicacao}.')
    elif per == 3:
        if n1 > n2:
            print(f'O maior valor é {n1}.')
        elif n2 > n1:
            print(f'O maior valor é {n2}.')
        else:
            print('Os dois valores são iguais.')
    elif per == 4:
        n1 = random.randint(1, 20)
        n2 = random.randint(1, 20)
        print(f'Os novos números aleatórios são {n1} e {n2}.')
    elif per == 5:
        print("Programa encerrado, obrigado por participar!")
        break
    elif per == 6:
        n1 = float(input('Digite um novo valor para n1: '))
        n2 = float(input('Digite um novo valor para n2: '))
        print(f'Números atualizados para: {n1} e {n2}')
    else:
        print("Opção inválida. Tente novamente.")

    # Pergunta se deseja encerrar
    sair = input("\nDeseja encerrar o programa? (S/N): ").strip().lower()
    if sair == 's':
        print("Encerrando o programa...")
        sleep(1)
        break

