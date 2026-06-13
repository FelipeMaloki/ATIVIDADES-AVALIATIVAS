print("=== CALCULADORA DE SOMA ===")

soma = 0

for i in range(1, 6):
    numero = float(input(f"Digite o {i}º número: "))
    soma = soma + numero 

print("\n=========================================")
print(f"A soma de todos os números é: {soma}")
print("=========================================")
