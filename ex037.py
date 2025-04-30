
from colorama import Fore, Style
print('-=-'* 20)
n =int(input(Fore.LIGHTMAGENTA_EX+ 'digite um número qualquer: '+Style.RESET_ALL))
print('-=-'* 20)
print('\033[7;40m[1] CONVERTER PARA BINARIO    \033[m')
print('\033[7;40m[2] CONVERTE PARA OCTAL       \033[m')
print('\033[7;40m[3] CONVERTER PARA HEXADECIMAL\033[m')
ques =int(input('qual a sua opção: '))
print('-=-'* 20)
bin =bin(n)
octal =oct(n)
hexa =hex(n)
if ques == 1:
    print('\033[0;30;41m o número {} convertido para bínario {}\033[m.'.format(n, bin))

elif ques == 2:
    print('\033[0;30;41m o número {} convertido para octal {}.\033[m'.format(n, octal))

elif ques == 3:
    print('\033[0;30;41m o número {} convertido para hexadecimal {}.\033[m'.format(n, hexa))

