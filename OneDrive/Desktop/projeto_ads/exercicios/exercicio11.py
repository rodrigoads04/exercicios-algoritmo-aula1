numero_str = input("Digite um número inteiro positivo: ")
soma = 0

for digito in numero_str:
    soma += int(digito)

print(f"A soma dos dígitos é: {soma}")