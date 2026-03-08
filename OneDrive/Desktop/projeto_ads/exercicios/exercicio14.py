qtd = int(input("Quantos números você quer digitar? "))

soma = 0
positivos = 0
negativos = 0
zeros = 0
maior = float('-inf')  
menor = float('inf')   

for i in range(qtd):
    num = float(input(f"Digite o {i+1}º número: "))
    
    soma += num
    
    if num > maior:
        maior = num
    if num < menor:
        menor = num
        
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1
    else:
        zeros += 1

media = soma / qtd if qtd > 0 else 0

print("\n--- Resultados ---")
print(f"Soma total: {soma}")
print(f"Média: {media:.2f}")
print(f"Maior: {maior}")
print(f"Menor: {menor}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Zeros: {zeros}")