from colorama import Style, Fore
from time import sleep
# p que mostre n em um int de 1/50 PARES
for c in range (1, 51):
     if c % 2== 0:
       print(f' os numeros no intervalo de 1 a 50 são respectivamentes: {c}')
       sleep(0.3)
print('-+-+-' * 20)

