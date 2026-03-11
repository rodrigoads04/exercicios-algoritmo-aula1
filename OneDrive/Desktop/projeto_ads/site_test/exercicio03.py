idade = int(input("Digite a idade da pessoa: "))

if idade >= 18:
    print("Você já pode tirar a carteira de motorista!")
else:
    print("Você ainda não pode dirigir. Falta(m) {} ano(s) para você poder dirigir.".format(18 - idade))