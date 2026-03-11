calculadora_desconto = float(input("Digite o valor da compra: R$ "))

if calculadora_desconto > 100:
    desconto = calculadora_desconto * 0.10
    valor_final = calculadora_desconto - desconto
    print(f"Desconto de 10% aplicado! Valor final: R$ {valor_final:.2f}")
else:
    print(f"Valor da compra: R$ {calculadora_desconto:.2f}. Sem desconto aplicado.")