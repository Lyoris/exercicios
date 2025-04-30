from colorama import Style, Fore
from time import sleep
print(Fore.LIGHTWHITE_EX + 'o seu calculo estará pronto jajá' + Style.RESET_ALL)
sleep(0.3)
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        print(Fore.GREEN + f'os números impares e divisiveis por 3 são respectivamente: {c}'+ Style.RESET_ALL)
        sleep(0.01)