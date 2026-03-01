limite = int(input("Digite um número inteiro positivo: "))

i = 0

print(f"Números pares de 0 até {limite}:")

while i <= limite:
    if i % 2 == 0:
        print(i)
    i += 1