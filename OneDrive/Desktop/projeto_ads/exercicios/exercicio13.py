base = int(input("Digite o número base: "))
limite = int(input("Digite o limite máximo: "))

print(f"Múltiplos de {base} entre 1 e {limite}:")

for i in range(base, limite + 1, base):
    print(i, end=" ")
print()