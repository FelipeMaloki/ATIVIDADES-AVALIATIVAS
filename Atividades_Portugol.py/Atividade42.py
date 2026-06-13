print("=== SISTEMA DE EMISSÃO DE BOLETOS ===")
print("Dias disponíveis para vencimento: 2, 5 ou 10")
print("========================================")

dia_vencimento = 0

dias_validos = [2, 5, 10]

while dia_vencimento not in dias_validos:
    dia_vencimento = int(input("Informe o melhor dia para o pagamento do boleto: "))

    if dia_vencimento not in dias_validos:
        print(" Dia inválido! Escolha apenas entre as opções: 2, 5 ou 10.\n")


print("\n========================================")
print(f"  Sucesso: Boleto registrado! (Vencimento dia {dia_vencimento})")
print("========================================")
