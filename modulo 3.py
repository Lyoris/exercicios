valores = []

# Lê 5 valores do usuário
for i in range(5):
    num = int(input(f"Digite o {i+1}º valor: "))
    valores.append(num)

# Encontra o maior e o menor valor
maior = max(valores)
menor = min(valores)

# Encontra as posições (índices) do maior e menor
pos_maior = [i for i, v in enumerate(valores) if v == maior]
pos_menor = [i for i, v in enumerate(valores) if v == menor]

# Exibe os resultados
print(f"\nValores digitados: {valores}")
print(f"Maior valor: {maior} nas posições: {pos_maior}")
print(f"Menor valor: {menor} nas posições: {pos_menor}")