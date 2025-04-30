#numeros pares
from time import sleep
print('CALCULANDO NÚMEROS PÁRES')
sleep(0.2)
s = 0
for n in range(1, 7):
    n =int(input('Digite um número: '))
    sleep(0.1)
    print('PROCESSANDO...')
    sleep(0.2)
    if n % 2==0:
        s += n
print(f'a soma entre os números pares são: {s}')
