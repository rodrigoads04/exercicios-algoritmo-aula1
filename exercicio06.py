idade = int(input("Digite a idade da pessoa: "))

if idade < 18:
    print("você ainda é menor de idade.")
elif idade >= 18 and idade < 60:
    print("você é um adulto.")
else:
    print("você é um idoso.")