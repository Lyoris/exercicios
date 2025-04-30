from random import randint
from time import sleep
import os

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_linha():
    print("-" * 40)

def jogo():
    vitorias = 0
    limpar_tela()
    print("=" * 40)
    print("         JOGO DO PAR OU ÍMPAR         ")
    print("=" * 40)

    while True:
        mostrar_linha()
        try:
            jogador = int(input("Digite um número entre 0 e 10: "))
            if jogador < 0 or jogador > 10:
                print("Número fora do intervalo. Tente novamente.")
                continue
        except ValueError:
            print("Digite um número válido.")
            continue

        escolha = ''
        while escolha not in ['P', 'I']:
            escolha = input("Par ou Ímpar? [P/I]: ").strip().upper()

        computador = randint(0, 10)
        total = jogador + computador
        resultado = 'P' if total % 2 == 0 else 'I'

        mostrar_linha()
        print(f"Você jogou {jogador} e o computador {computador}. Total = {total}")
        print("Resultado: PAR" if resultado == 'P' else "Resultado: ÍMPAR")
        mostrar_linha()

        if escolha == resultado:
            print("Você venceu!")
            vitorias += 1
        else:
            print("Você perdeu!")
            break

        sleep(1)

    mostrar_linha()
    print(f"FIM DE JOGO! Vitórias consecutivas: {vitorias}")
    mostrar_linha()

if __name__ == "__main__":
    jogo()