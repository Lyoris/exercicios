import random
import time
from colorama import Fore, Style, init
# Importa a biblioteca random para gerar números aleatórios
# Importa time para adicionar pausas no jogo (como a digitação lenta)
# Importa colorama para colorir o texto no terminal e melhorar a experiência visual

# Inicializando o colorama
init(autoreset=True)
# Inicializa o colorama, com "autoreset=True" para garantir que a cor do texto seja resetada automaticamente após cada uso

# Função para digitar o texto lentamente
def digitar(texto, delay=0.05):
    for letra in texto:  # Itera sobre cada letra do texto
        print(letra, end='', flush=True)  # Imprime a letra sem pular linha
        time.sleep(delay)  # Pausa para dar o efeito de digitação lenta
    print()  # Adiciona uma nova linha ao final

# Classe que representa uma partida do jogo
class Partida:
    def __init__(self, numero_secreto):
        self.numero_secreto = numero_secreto  # Número secreto que o jogador deve adivinhar
        self.tentativas = 0  # Contador de tentativas do jogador
        self.acertou = False  # Flag que indica se o jogador acertou o número

    def jogar(self):
        # Início do jogo, com uma introdução para o jogador
        digitar(Fore.CYAN + "Eu escolhi um número entre 1 e 100... tente adivinhar!")
        time.sleep(1)  # Pausa de 1 segundo antes de continuar

        while not self.acertou:  # Enquanto o jogador não acertar o número
            try:
                palpite = int(input(Fore.YELLOW + "Seu palpite: "))  # Solicita o palpite do jogador
            except ValueError:  # Caso o jogador não digite um número válido
                digitar(Fore.RED + "Digite um número válido!")  # Exibe uma mensagem de erro
                continue  # Volta ao início do laço para pedir o palpite novamente

            self.tentativas += 1  # Incrementa o número de tentativas

            if palpite < self.numero_secreto:  # Se o palpite for menor que o número secreto
                digitar(Fore.BLUE + "Mais... tente um número MAIOR.")  # Dá uma dica para o jogador
            elif palpite > self.numero_secreto:  # Se o palpite for maior que o número secreto
                digitar(Fore.MAGENTA + "Menos... tente um número MENOR.")  # Outra dica
            else:  # Caso o jogador acerte o número
                digitar(Fore.GREEN + f"PARABÉNS! Você acertou em {self.tentativas} tentativas!")
                # playsound('vitoria.mp3')  # Opcional: Se houver um som de vitória, pode ser tocado aqui
                self.acertou = True  # Marca que o jogador acertou o número

# Função que exibe o menu principal
def menu():
    print(Fore.LIGHTCYAN_EX + "\n--- JOGO ADIVINHA O NÚMERO ---")  # Título do jogo
    print("[1] Jogar")  # Opção para iniciar uma nova partida
    print("[2] Ver Histórico")  # Opção para ver o histórico de partidas
    print("[3] Sair")  # Opção para sair do jogo

# Função para mostrar o histórico das partidas jogadas
def mostrar_historico(historico):
    print(Fore.LIGHTMAGENTA_EX + "\n=== Histórico de Partidas ===")  # Título do histórico
    if not historico:  # Se não houver partidas jogadas
        digitar(Fore.RED + "Nenhuma partida jogada ainda.")  # Exibe uma mensagem informando
    else:  # Se houver partidas no histórico
        for i, partida in enumerate(historico):  # Para cada partida no histórico
            status = Fore.GREEN + "Acertou" if partida.acertou else Fore.RED + "Não Acertou"  # Define a cor conforme o resultado
            print(f"Partida {i+1}: {status} em {partida.tentativas} tentativas.")  # Exibe o status da partida

# Função principal que executa o jogo
def main():
    historico = []  # Lista que armazenará o histórico de partidas
    personagem = Fore.LIGHTBLUE_EX + "[Narrador]: "  # Personagem (Narrador) com cor azul claro

    # Introdução do jogo
    digitar(personagem + "Olá, aventureiro!")
    time.sleep(0.8)
    digitar(personagem + "Preparado para testar sua sorte e inteligência?")
    time.sleep(1)

    while True:  # Loop principal que mantém o jogo em execução até o jogador escolher sair
        menu()  # Exibe o menu principal
        opcao = input(Fore.LIGHTYELLOW_EX + "Escolha uma opção: ")  # Solicita a escolha do jogador

        if opcao == '1':  # Se o jogador escolher jogar
            numero = random.randint(1, 100)  # Gera um número secreto aleatório entre 1 e 100
            partida = Partida(numero)  # Cria uma nova partida com o número secreto gerado
            partida.jogar()  # Inicia o jogo
            historico.append(partida)  # Adiciona a partida ao histórico
        elif opcao == '2':  # Se o jogador escolher ver o histórico
            mostrar_historico(historico)  # Exibe o histórico de partidas
        elif opcao == '3':  # Se o jogador escolher sair
            digitar(personagem + "Até mais, jovem guerreiro!")  # Mensagem de despedida
            # playsound('despedida.mp3')  # Opcional: Som de despedida
            break  # Encerra o loop e o jogo
        else:  # Se o jogador escolher uma opção inválida
            digitar(Fore.RED + "Opção inválida, tente novamente.")  # Mensagem de erro

# Executa o jogo
if __name__ == "__main__":
    try:
        main()  # Chama a função principal para iniciar o jogo
    except Exception as e:  # Se ocorrer algum erro inesperado
        print(Fore.RED + f"\nErro inesperado: {e}")  # Exibe a mensagem de erro
    finally:
        input(Fore.LIGHTBLACK_EX + "\nPressione ENTER para sair...")  # Espera o jogador pressionar ENTER antes de sair