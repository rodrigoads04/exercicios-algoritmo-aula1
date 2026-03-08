n = int(input("Digite um número inteiro n: "))

soma_pares = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        soma_pares += i

print(f"A soma dos números pares de 1 até {n} é: {soma_pares}")
