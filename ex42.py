from datetime import date
from colorama import Style, Fore
from time import sleep
# faa um progrma q mostre uma cont regress para
# estouro de fogos de artificios
#de 0 a 10 e p/ de 1s
print(Fore.WHITE+ '-==-'*20 + Style.RESET_ALL)
fogos =print(Fore.RED +'os fogos serão acesos em 10 segundos'+Style.RESET_ALL)
print('-==-'*20)
sleep(0.3)
for c in range(1, 11):
    print(Fore.MAGENTA +str(c), end="")
    print(Style.RESET_ALL)
    sleep(1)
print(Fore.GREEN + 'aproveite a queima dos fogos' + Style.RESET_ALL)