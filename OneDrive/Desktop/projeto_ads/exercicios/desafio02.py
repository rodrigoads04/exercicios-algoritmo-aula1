n = int(input("Digite um número inteiro n: "))

soma_pares = 0
soma_impares = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        soma_pares += i
    else:
        soma_impares += i

print(f"Soma das posições ímpares (1ª, 3ª...): {soma_impares}")
print(f"Soma das posições pares (2ª, 4ª...): {soma_pares}")