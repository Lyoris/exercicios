valores = []
while True:
    valores.append(int(input('Digite um valor')))
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Voce digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f"os valores digitados em ordem decrescente são {valores}")
if 5 in valores:
    print('o valor 5 faz parte da lista')
else:
    print("o valor 5 não faz parte da lista")