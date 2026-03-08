texto = input("Digite um texto: ")
caractere = input("Digite o caractere que deseja contar: ")

texto_min = texto.lower()
caractere_min = caractere.lower()

contador = 0

for c in texto_min:
    if c == caractere_min:
        contador += 1

print(f"O caractere '{caractere}' aparece {contador} vez(es) no texto.")