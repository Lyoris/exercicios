import random
from time import sleep
p = random.randint(0, 5) # faz o pc "pensar"
print('-=-' * 20)
print('vou pensar em um numero entre 0 e 5. tente adivinhar....')
print('-=-' * 20)
jo =int(input('em que número eu pensei? '))#jogador tenta adivinhar
print('PROCESSANDO...')
sleep(1.5)
while jo not in {p}:
    print('tinha funcionado, mas apaguei sem querer, tmnnc')
    sleep(0.5)
print(f"meu numero escolhido foi {p}\nvocê é um genio!!!")
print('-=' * 15)