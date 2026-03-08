texto: str = input("Digite um texto: ")

texto_invertido = ""

for caractere in texto:
    texto_invertido = caractere + texto_invertido

print(f"Versão invertida: {texto_invertido}")