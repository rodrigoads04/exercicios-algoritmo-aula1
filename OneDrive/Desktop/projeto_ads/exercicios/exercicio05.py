qtd = int(input("Quantos números você quer digitar? "))

primeiro_num = float(input("Digite o 1º número: "))
maior = primeiro_num
menor = primeiro_num

for i in range(2, qtd + 1):
    num = float(input(f"Digite o {i}º número: "))
    
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(f"\nO maior número digitado foi: {maior}")
print(f"O menor número digitado foi: {menor}")
