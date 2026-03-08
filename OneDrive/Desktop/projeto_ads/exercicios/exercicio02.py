n = int(input("Digite um número inteiro n: "))

soma = 0

# Percorre de 1 até n
for i in range(1, n + 1):
    soma += i

print(f"A soma de 1 até {n} é: {soma}")
