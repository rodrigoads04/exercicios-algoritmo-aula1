qtd = int(input("Quantas notas você quer informar? "))

soma_notas = 0

for i in range(1, qtd + 1):

    while True:
        nota = float(input(f"Digite a {i}ª nota (0 a 10): "))
        
        if 0 <= nota <= 10:
            break 
        else:
            print("Nota inválida! Por favor, digite um valor entre 0 e 10.")
            
    soma_notas += nota

media = soma_notas / qtd

print(f"\nA média final das {qtd} notas é: {media:.2f}")