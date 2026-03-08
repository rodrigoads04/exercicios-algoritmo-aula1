n = int(input("Digite um número inteiro n: "))

pares = 0
impares = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1

# 4. Exibe os resultados
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
