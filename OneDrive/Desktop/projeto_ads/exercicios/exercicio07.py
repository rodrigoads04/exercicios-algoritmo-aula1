frase = input("Digite uma frase: ")
              
vogais = "aeiou"

total_vogais = sum(1 for letra in frase.lower() if letra in vogais)

print(f"A frase contém um total de {total_vogais} vogais.")