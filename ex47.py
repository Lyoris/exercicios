frase = input('Digite uma frase: ').strip().lower()
frase = ''.join(frase.split())

if frase == frase[::-1]:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo.')